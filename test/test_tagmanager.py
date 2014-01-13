__author__ = 'likun'

import unittest
from mock import Mock
from datetime import datetime
from core import database
from core import models


class TagManagerTest(unittest.TestCase):
	def setUp(self):
		self.tag_mag = models.TagManager()
		self.tag = models.BlogTag("test")
		self.db = Mock()
		self.db.tag = Mock()
		models.db = self.db

	def test_remove(self):
		self.tag_mag.remove(123)
		models.db.tag.remove.assert_called_with({"_id":123})

	def test_add(self):
		self.tag.to_json = Mock()
		self.tag.to_json.return_value = {"_id":122}
		self.tag_mag.add(self.tag)
		self.db.tag.insert.assert_called_with({"_id":122})

	def test_edit(self):
		self.tag_mag.edit(123,"test")
		models.db.tag.update.assert_called_with({"_id":123},{"name":"test"})

	def test_get(self):
		self.tag_mag.get(123)
		models.db.tag.find_one.assert_called_with({"_id":123})

if __name__ == '__main__':
    unittest.main()
