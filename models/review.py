#!/usr/bin/python3
"""Review class inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ This is the Review model"""
    place_id = ""
    user_id = ""
    text = ""
