__author__ = 'likun'

import unittest
from mock import Mock
from datetime import datetime
from core import database
from core import models


class CategoryManagerTest(unittest.TestCase):
	def setUp(self):
		self.category_mag = models.CategoryManager()
		self.category = models.BlogCategory("test")
		self.db = Mock()
		self.db.category = Mock()
		models.db = self.db

	def test_remove(self):
		self.category_mag.remove(123)
		models.db.category.remove.assert_called_with({"_id":123})

	def test_add(self):
		self.category.to_json = Mock()
		self.category.to_json.return_value = {"_id":122}
		self.category_mag.add(self.category)
		self.db.category.insert.assert_called_with({"_id":122})

	def test_edit(self):
		self.category_mag.edit(123,"test")
		models.db.category.update.assert_called_with({"_id":123},{"name":"test"})

	def test_get(self):
		self.category_mag.get(123)
		models.db.category.find_one.assert_called_with({"_id":123})

if __name__ == '__main__':
    unittest.main()
