import os, json


config = os.path.dirname(__file__) + '/config.json'


def get(key):
	global config
	if not os.path.isfile(config):
		return ''
	with open(config, 'r') as f:
		config = json.load(f)
		if key in config:
			return config[key]
		f.close()


def set(key, val):
	global config
	if not isinstance(val, str):
		return False

	if not os.path.isfile(config):
		with open(config, 'a') as f:
			f.write('{}')
			f.close()

	with open(config, 'r+') as f:
		data = json.load(f)
		data[key] = val
		f.seek(0)  # <--- should reset file position to the beginning.
		json.dump(data, f, indent=4)
		f.truncate()  # remove remaining part
		f.close()
