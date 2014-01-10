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
        return result

class TagManager():
    def add(self,tag):
        db.tag.insert(tag.to_json())

    def remove(self,id):
        db.tag.remove({"_id":id})

    def edit(self,id,name):
        db.tag.update({"_id":id},{"name":name})

    def get(self,id):
        return db.tag.find_one({"_id":id})


class Blog():

    def __init__(self,title,tags,category,content,public,created_time = datetime.now()):
        self.title = title
        self.tags = tags        
        self.category = category   
        self.content = content    
        self.counts = 0     
        self.update_time = created_time
        self.public = public     
        self.created_time = created_time

    def to_json():
        return { "title":self.title,"tags":self.tags,"category":self.category,
                "content":self.content,"counts":self.counts,"update_time":self.update_time,
                "public":self.public,"created_time":self.created_time}

class BlogManager():
    def add(self,blog):
        db.blog.insert(blog.to_json())

    def remove(self,id):
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

    def to_json():
        return {"name":self.name,"created_time":self.created_time}

class CategoryManager():
    def add(self,category):
        db.category.insert(category.to_json())

    def remove(self,id):
        db.category.remove({"_id":id})

    def edit(self,id,name):
        db.category.update({"_id":id},{"name":name})

    def get(self,id):
        return db.category.find_one({"_id":id})
