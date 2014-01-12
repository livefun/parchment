__author__ = 'likun'

import unittest
from mock import Mock
from datetime import datetime
from core import database
from core import models


class BlogManagerTest(unittest.TestCase):
	def setUp(self):
		self.blog_mag = models.BlogManager()
		self.blog = models.Blog("test","test","test","test","test","test")
		self.db = Mock()
		self.tag = Mock()
		self.db.blog = Mock()
		models.db = self.db

	def test_remove(self):
		self.blog_mag.remove(123)
		models.db.blog.remove.assert_called_with({"_id":123})

	def test_add(self):
		self.blog.to_json = Mock()
		self.blog.to_json.return_value = {"_id":122}
		self.blog_mag.add(self.blog)
		self.db.blog.insert.assert_called_with({"_id":122})

	def test_edit(self):
		self.blog_mag.edit(123,"test","test","test","test","test")
		models.db.blog.update.assert_called_with({"_id":123},{"title":"test","tag":"test","category":"test","content":"test","update_time":"test"})

	def test_get_by_id(self):
		self.blog_mag.get_by_id(123)
		models.db.blog.find_one.assert_called_with({"_id":123})

	# def test_get_by_tag(self):
	# 	self.blog_mag.get_by_tag(123)
	# 	models.db.blog.find.return_value = 1
	# 	models.db.blog.find.assert_called_with({"tags":[123]})

	# def test_get_by_id(self):
	# 	self.blog_mag.get_by_id(123)
	# 	models.db.blog.find.assert_called_with({"category":123})

if __name__ == '__main__':
    unittest.main()
