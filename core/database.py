from pymongo import Connection


def db_session():
    connection = Connection("localhost", 27017)
    return connection['blog']