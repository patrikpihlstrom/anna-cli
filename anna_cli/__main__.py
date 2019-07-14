#!/usr/local/bin/python3

import click
import requests
import json

import query
from group import Anna
import persist


@click.group(Anna)
def cli():
	"""
	CLI for the anna API   github.com/patrikpihlstrom/anna-api.git
	"""
	pass


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('action')
@click.argument('remote', required=False)
def remote(action, remote=None):
	"""
	get or set the remote
	:param action:
	:param remote:
	:return:
	"""
	if action == 'set':
		persist.set('remote', remote)
	elif action == 'get':
		click.echo(persist.get('remote'))


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('action')
@click.argument('token', required=False)
def token(action, token=None):
	"""
	get or set the token
	:param action:
	:param token:
	:return:
	"""
	if action == 'set':
		persist.set('token', token)
	elif action == 'get':
		click.echo(persist.get('token'))


def echo(response):
	if query.is_json(response.content):
		click.echo(json.dumps(response.json(), indent=4, sort_keys=True))
	else:
		click.echo(response.content)


@click.argument('email')
@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
def auth(email):
	"""
	get an authentication token from the remote server
	:return:
	"""
	response = requests.get(persist.get('remote') + '/auth/token', headers={'Authorization': email})
	if query.is_json(response.content) and 'token' in response.json():
		persist.set('token', response.json()['token'])
	echo(response)


def get_authentication_header():
	return {'Authorization': 'Bearer ' + persist.get('token')}


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--drivers', '-d', default=[])
@click.option('--sites', '-s', default=[])
def push(drivers, sites):
	"""
	push a new job to the queue
	:param drivers:
	:param sites:
	:return:
	"""
	job = query.job(drivers, sites)
	response = requests.post(persist.get('remote') + '/job/push', json=job, headers=get_authentication_header())
	echo(response)


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--id', '-i', default=[])
@click.option('--container', '-c', default=[])
@click.option('--driver', '-d', default=[])
@click.option('--site', '-s', default=[])
@click.option('--status', '-S', default=[])
@click.option('--tag', '-t', default=[])
def get(id, container, driver, site, status, tag):
	"""
	get jobs based on the provided filter
	:param id:
	:param container:
	:param driver:
	:param site:
	:param status:
	:param tag:
	:return:
	"""
	filter = query.filter(id=id, container=container, driver=driver, site=site, status=status, tag=tag)
	response = requests.get(persist.get('remote') + '/job/get', json=filter, headers=get_authentication_header())
	echo(response)


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--id', '-i', default=[])
@click.option('--container', '-c', default=[])
@click.option('--driver', '-d', default=[])
@click.option('--site', '-s', default=[])
@click.option('--status', '-S', default=[])
@click.option('--tag', '-t', default=[])
def rm(id, container, driver, site, status, tag):
	"""
	get jobs based on the provided filter
	:param id:
	:param container:
	:param driver:
	:param site:
	:param status:
	:param tag:
	:return:
	"""
	filter = query.filter(id=id, container=container, driver=driver, site=site, status=status, tag=tag)
	response = requests.post(persist.get('remote') + '/job/rm', json=filter, headers=get_authentication_header())
	echo(response)


if __name__ == '__main__':
	cli()
