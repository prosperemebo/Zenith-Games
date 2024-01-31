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
    products = relationship(
        "Product", secondary=product_category_association, backref="categories"
    )


    def __init__(self, *args, **kwargs):
        """ Initialize Category """
        super().__init__(*args, **kwargs)
        
    @property
    def products(self):
        """getter attribute returns the list of Product instances"""
        from models.product import Product

        product_list = []
        products = models.storage.all(Product)

        for product in products.values():
            category_ids = product.categories.split(',')
            
            if self.id in category_ids:
                product_list.append(product)
        return product_list
