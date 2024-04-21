#!/usr/bin/python3
"""this is the state"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """this shows state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """this starts state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def fun(self):
            """this outputs items in state"""
            mtx = []
            pes = models.storage.all(City)
            for city in pes.values():
                if city.state_id == self.id:
                    mtx.append(city)
            return mtx
