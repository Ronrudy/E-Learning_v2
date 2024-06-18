#!/usr/bin/python
""" holds class Badge"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Badge(BaseModel, Base):
    """Representation of badge """
    if models.storage_t == "db":
        __tablename__ = 'badges'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        activity_id = Column(String(60), ForeignKey('activities.id'), nullable=False)
        badge_name = Column(String(128))
        student_id = Column(String(60), ForeignKey('student.id'), nullable=False)
        
        # Relationships

    else:
        user_id = ""
        activity_id = ""
        badge_name = ""
        date_awarded = ""
        student_id = ""

    def __init__(self, *args, **kwargs):
        """initializes badge"""
        super().__init__(*args, **kwargs)
