#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from sqlalchemy import or_, func
import models
from models.base_model import BaseModel, Base
from models.category import Category
from models.product import Product
from os import getenv
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Category": Category, "Product": Product}

load_dotenv()


class DBStorage:
    """interaacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = getenv("MYSQL_USER")
        MYSQL_PWD = getenv("MYSQL_PWD")
        MYSQL_HOST = getenv("MYSQL_HOST")
        MYSQL_DB = getenv("MYSQL_DB")
        ENV = getenv("ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB
            )
        )
        # if ENV == "test":
        #     Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, page=1, per_page=100, **kwargs):
        """query on the current database session"""
        new_dict = {}
        
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                query = self.__session.query(classes[clss])

                if kwargs:
                    query = query.filter_by(**kwargs)
                    
                # offset = (page - 1) * per_page
                # query = query.offset(offset).limit(per_page)

                objs = query.all()

                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value

        return None

    def get_by_field(self, cls, field_str, value):
        """
        Returns the object based on the class name and the field value, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_objects = models.storage.all(cls)
        fields = field_str.split(" ")

        for obj in all_objects.values():
            match = False

            for field in fields:
                if not hasattr(obj, field):
                    match = False
                    break

                field_value = getattr(obj, field)

                if field_value == value:
                    match = True
                    break

            if match:
                return obj

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def search(self, cls, query_columns, query_value, **kwargs):
        """Search objects in storage"""
        new_dict = {}

        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                query = self.__session.query(classes[clss])

                if query_columns:
                    column_filters = [
                        getattr(classes[clss], column).ilike(f"%{query_value}%")
                        for column in query_columns
                    ]
                    query = query.filter(or_(*column_filters))

                if kwargs:
                    query = query.filter_by(**kwargs)
                    
                relevance_score = sum([
                    func.lower(getattr(classes[clss], column)) == query_value.lower() 
                    for column in query_columns
                ])
                query = query.order_by(relevance_score.desc())

                objs = query.all()

                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj

        return new_dict
