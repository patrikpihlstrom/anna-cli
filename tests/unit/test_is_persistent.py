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
		set('remote', '')
		set('token', '')
		self.assertEqual('', get('remote'))
		self.assertEqual('', get('token'))
		rand = ''.join(random.choice(string.uppercase + string.lowercase + string.digits) for i in range(64))
		set('remote', rand)
		self.assertEqual(rand, get('remote'))
		rand = ''.join(random.choice(string.uppercase + string.lowercase + string.digits) for i in range(64))
		set('token', rand)
		self.assertEqual(rand, get('token'))
