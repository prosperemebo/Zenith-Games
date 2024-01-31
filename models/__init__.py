#!/usr/bin/python3
"""
initialize the models module
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
