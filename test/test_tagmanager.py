__author__ = 'likun'

import unittest
from mock import Mock,MagicMock
from datetime import datetime
from core import database
db = Mock()
from core import models


class TagManagerTest(unittest.TestCase):

    def test_del(self):
        tag = models.TagManager()
        tag.dele(123)        

if __name__ == '__main__':
    unittest.main()
