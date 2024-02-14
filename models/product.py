#!/usr/bin/python
""" Product Class Implementation """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table, Integer, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    """Representation of Product"""

    __tablename__ = "products"
    label = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    summary = Column(LONGTEXT)
    description = Column(LONGTEXT)
    cover_image = Column(String(255), nullable=True)
    images = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    source_id = Column(String(60), nullable=False, unique=True)
    status = Column(
        Enum("out_of_stock", "draft", "publish", "deleted"), default="publish"
    )
    categories = Column(String(1024), nullable=False, default='')

    def __init__(self, *args, **kwargs):
        """Initialize Product"""
        super().__init__(*args, **kwargs)
        
    @property
    def categories_list(self):
        """getter attribute returns the list of Category instances"""
        category_ids = self.categories.split(',')
        return category_ids
