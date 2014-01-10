from pymongo import  Connection


def db_session():
    exec('connection = %s' % Connection("localhost", 27017))
    return connection['blog']