#!/usr/bin/python3
"""Defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User by various attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
