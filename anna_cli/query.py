import json


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
	if is_json(id):
		result['id'] = json.loads(id)
	elif id is not None and len(id) > 0:
		result['id'] = str(id)
	if is_json(container):
		result['container'] = json.loads(container)
	elif container is not None and len(container) > 0:
		result['container'] = str(container)
	if is_json(driver):
		result['driver'] = json.loads(driver)
	elif driver is not None and len(driver) > 0:
		result['driver'] = str(driver)
	if is_json(site):
		result['site'] = json.loads(site)
	elif site is not None and len(site) > 0:
		result['site'] = str(site)
	if is_json(status):
		result['status'] = json.loads(status)
	elif status is not None and len(status) > 0:
		result['status'] = str(status)
	if is_json(tag):
		result['tag'] = json.loads(tag)
	elif tag is not None and len(tag) > 0:
		result['tag'] = str(tag)
	return result

