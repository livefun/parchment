# -*- coding:utf-8 -*-
from datetime import datetime
from core import database

db = database.db_session()

class BlogTag():

    def __init__(self,name,created_time =datetime.now()):
        self.name = name
        self.created_time = created_time


    def to_json(self,new_dict={}):
        result = {"name":self.name,"created_time":self.created_time}
        for k in new_dict:
            result[k] = new_dict.get(k)
        return result

class TagManager():

    def dele(self,id):
        db.tag.remove({"_id":id})

    def edit(self,id,name):
        db.tag.update({"_id":id},{"name":name})

    def get(self,id):
        return db.tag.find_one({"_id":id})


class Blog():

    def __init__(self,title,tags,category,content,counts,update_time,public,created_time = datetime.now()):
        self.title = title
        self.tags = tags        
        self.category = category   
        self.content = content    
        self.counts = counts     
        self.update_time = update_time
        self.public = public     
        self.created_time = created_time

    def to_json():
        return {"title":self.title,"tags":this.tags}

class BlogManager():

    def dele(self,id):
        db.blog.remove({"_id":id})

    def edit(self,id,title,tag,category,content,update_time = datetime.now()):
        db.blog.update({"_id":id},{"title":title,"tag":tag,"category":category,"content":content,"update_time":update_time})

    def get_by_id(self,id):
        return db.blog.find_one({"_id":id})

    def get_by_tag(self,tag): 
        return [blog for blog in db.blog.find({"tags":[tag]})]

    def get_by_category(self,category): 
        return [blog for blog in db.blog.find({"category":category})]

class BlogCategory():
    def __init__(self,name,created_time =datetime.now()):
        self.name = name
        self.created_time = created_time

class CategoryManager():
    def dele(self,id):
        db.category.remove({"_id":id})

    def edit(self,id,name):
        db.category.update({"_id":id},{"name":name})

    def get(self,id):
        return db.category.find_one({"_id":id})
