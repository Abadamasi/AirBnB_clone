#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent an city.

    Attributes:
        state_id (str): The state id.
    """

    state_id = ""
    name = ""
