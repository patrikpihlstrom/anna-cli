#!/usr/bin/python

import click
import requests
import json
from pprint import pprint

from group import Anna, PythonLiteralOption
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
	click.echo(response.json())


def is_json(string):
	try:
		json.loads(string)
	except ValueError:
		return False
	except TypeError:
		return False
	return True


@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--drivers', '-d', default=[])
@click.option('--sites', '-s', default=[])
def push(drivers, sites):
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
	job = {}
	if is_json(drivers):
		job['drivers'] = json.loads(drivers)
	elif drivers is not None and len(drivers) > 0:
		job['drivers'] = str(drivers)
	if is_json(sites):
		job['sites'] = json.loads(sites)
	elif sites is not None and len(sites) > 0:
		job['sites'] = str(sites)
	if not isinstance(job['drivers'], list):
		job['drivers'] = [job['drivers']]
	if not isinstance(job['sites'], list):
		job['sites'] = [job['sites']]
	print(job)
	pprint(requests.post(persist.get('remote') + '/v1.0/push', json=job).json())


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
	filter = {}
	if is_json(id):
		filter['id'] = json.loads(id)
	elif id is not None and len(id) > 0:
		filter['id'] = str(id)
	if is_json(container):
		filter['container'] = json.loads(container)
	elif container is not None and len(container) > 0:
		filter['container'] = str(container)
	if is_json(driver):
		filter['driver'] = json.loads(driver)
	elif driver is not None and len(driver) > 0:
		filter['driver'] = str(driver)
	if is_json(site):
		filter['site'] = json.loads(site)
	elif site is not None and len(site) > 0:
		filter['site'] = str(site)
	if is_json(status):
		filter['status'] = json.loads(status)
	elif status is not None and len(status) > 0:
		filter['status'] = str(status)
	if is_json(tag):
		filter['tag'] = json.loads(tag)
	elif tag is not None and len(tag) > 0:
		filter['tag'] = str(tag)
	click.echo(requests.get(persist.get('remote') + '/v1.0/get', json=filter).json())


if __name__ == '__main__':
	cli()
