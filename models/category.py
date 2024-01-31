#!/usr/bin/python
""" category Class Implementation """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.product import product_category_association

class Category(BaseModel, Base):
    """ Representation of Category """

    __tablename__ = 'categories'
    label = Column(String(1024), nullable=False)
    slug = Column(String(1024), nullable=False)
    summary = Column(String(1024), nullable=False, default='')
    parent_id = Column(String(60), ForeignKey('categories.id'), nullable=True)
    source_id = Column(String(60), nullable=False)
    status = Column(Enum('draft', 'publish', 'deleted'), default='deleted')
    products = relationship('Product', secondary=product_category_association, back_populates='categories')


    def __init__(self, *args, **kwargs):
        """ Initialize Category """
        super().__init__(*args, **kwargs)
