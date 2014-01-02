# -*- coding:utf-8 -*-
from datetime import datetime

class Tag():
    def __init__(self,name,created_time =datetime.now()):
        self.name = name
        self.created_time = created_time
