#!/usr/bin/python3
"""
this is the database storage file
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

variables = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """this works with mysql database"""
    __engine = None
    __session = None

    def __init__(self):
        """this starts the database"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def fun(self, res=None):
        """this is the curr database"""
        xy = {}
        for res2 in variables:
            if res is None or res is variables[res2] or res is res2:
                abxs = self.__session.query(variables[res2]).all()
                for obj in abxs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    xy[key] = obj
        return (xy)

    def fun2(self, obj):
        """this is object curr database"""
        self.__session.add(obj)

    def fun3(self):
        """this effects changes in the database"""
        self.__session.commit()

    def fun4(self, obj=None):
        """this removes the curr database"""
        if obj is not None:
            self.__session.delete(obj)

    def fun5(self):
        """this restarts the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def fun6(self):
        """this invokes the remove function"""
        self.__session.remove()
