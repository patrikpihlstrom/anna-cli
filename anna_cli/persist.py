import os, json


def get(key):
	if not os.path.isfile('config.json'):
		return ''
	with open('config.json', 'r') as f:
		config = json.load(f)
		if key in config:
			return config[key]
		f.close()


def set(key, val):
	if not isinstance(val, str):
		return False

	if not os.path.isfile('config.json'):
		with open('config.json', 'a') as f:
			f.write('{}')
			f.close()

	with open('config.json', 'r+') as f:
		data = json.load(f)
		data[key] = val
		f.seek(0)  # <--- should reset file position to the beginning.
		json.dump(data, f, indent=4)
		f.truncate()  # remove remaining part
		f.close()
