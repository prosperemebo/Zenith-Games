#!/usr/bin/python
""" Product Class Implementation """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table, Integer, Enum
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

product_category_association = Table(
    'product_category_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


class Product(BaseModel, Base):
    """ Representation of Product """

    __tablename__ = 'products'
    label = Column(String(1024), nullable=False)
    slug = Column(String(1024), nullable=False)
    summary = Column(String(1024), nullable=False, default='')
    description = Column(String(1024), nullable=False, default='')
    cover_image = Column(String(1024), nullable=True)
    images = Column(String(1024), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    source_id = Column(String(60), nullable=False)
    status = Column(Enum('out_of_stock', 'draft', 'publish', 'deleted'), default='publish')
    categories = relationship(
        'Category', secondary=product_category_association, back_populates='products')

    def __init__(self, *args, **kwargs):
        """ Initialize Product """
        super().__init__(*args, **kwargs)
