import random
import string
import unittest

from anna_cli.persist import get, set


class TestPersist(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_get_set(self):
		set('endpoint', '')
		set('token', '')
		self.assertEqual('', get('endpoint'))
		self.assertEqual('', get('token'))
		rand = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(64))
		set('endpoint', rand)
		self.assertEqual(rand, get('endpoint'))
		rand = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(64))
		set('token', rand)
		self.assertEqual(rand, get('token'))
