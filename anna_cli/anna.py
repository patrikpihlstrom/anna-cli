#!/usr/bin/python

import click
import requests
import json
from pprint import pprint

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


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
def auth():
	"""
	get an authentication token from the remote server
	:return:
	"""
	response = requests.get(persist.get('remote') + '/auth/token')
	click.echo(json.dumps(response.json(), indent=4, sort_keys=True))


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
	click.echo(json.dumps(requests.post(persist.get('remote') + '/v1.0/push', json=job).json(), indent=4, sort_keys=True))


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
	click.echo(json.dumps(requests.get(persist.get('remote') + '/v1.0/get', json=filter).json(), indent=4, sort_keys=True))


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
	click.echo(json.dumps(requests.post(persist.get('remote') + '/v1.0/rm', json=filter).json(), indent=4, sort_keys=True))


if __name__ == '__main__':
	cli()
