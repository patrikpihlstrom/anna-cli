import json
from pprint import pprint


def is_json(string):
	try:
		json.loads(string)
	except ValueError:
		return False
	except TypeError:
		return False
	return True


def job(drivers, sites):
	result = {}
	if is_json(drivers):
		result['drivers'] = json.loads(drivers)
	elif drivers is not None and len(drivers) > 0:
		result['drivers'] = str(drivers)
	if is_json(sites):
		result['sites'] = json.loads(sites)
	elif sites is not None and len(sites) > 0:
		result['sites'] = str(sites)
	if not isinstance(result['drivers'], list):
		result['drivers'] = [result['drivers']]
	if not isinstance(result['sites'], list):
		result['sites'] = [result['sites']]
	return result


def filter(id, container, driver, site, status, tag):
	result = {}
	if id is not None and len(id) > 0:
		result['id'] = str(id).split(',')
	if container is not None and len(container) > 0:
		result['container'] = str(container).split(',')
	if driver is not None and len(driver) > 0:
		result['driver'] = str(driver).split(',')
	if site is not None and len(site) > 0:
		result['site'] = str(site).split(',')
	if status is not None and len(status) > 0:
		result['status'] = str(status).split(',')
	if tag is not None and len(tag) > 0:
		result['tag'] = str(tag).split(',')
	pprint(result)
	return result

