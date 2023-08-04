#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    """User class representation."""
    # Define the necessary columns for the User table
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    # Add any other columns specific to the User class



storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
