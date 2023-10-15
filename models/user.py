#!/usr/bin/python3
"""class User inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """ This is the Class user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
