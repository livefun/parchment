# -*- coding:utf-8 -*-
from datetime import datetime

class BlogTag():

    def __init__(self,name,created_time =datetime.now()):
        self.name = name
        self.created_time = created_time

    def to_json(self,new_dict={}):
        result = {"name":self.name,"created_time":self.created_time}
        for k in new_dict:
            result[k] = new_dict.get(k)
        return result

class TagManger():
    pass

class Blog():
    pass

class BlogManger():
    pass

class BlogType():
    pass

class TypeManger():
    pass
