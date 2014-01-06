__author__ = 'livefun'

import unittest
from mock import Mock,MagicMock
from datetime import datetime
from core import models

class TagTest(unittest.TestCase):

    def test_init(self):
        dt = datetime.now()
        tag = models.BlogTag('first_blog',dt)
        assert "first_blog" == tag.name
        assert dt == tag.created_time

    def test_to_json(self):
        dt = datetime.now()
        tag = models.BlogTag('first_blog',dt)
        assert {"name":"first_blog",'created_time':dt} == tag.to_json()


if __name__ == '__main__':
    unittest.main()
