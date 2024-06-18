#!/usr/bin/python3
""" Sudent Module for EL project """
import models
import json
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Student(BaseModel, Base):
    """Representation of Student profile """
    if models.storage_t == "db":
        __tablename__ = 'student'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        age = Column(Integer, nullable=False)
        stage = Column(String(60), nullable=False)
        activityCategory_id = Column(String(60), ForeignKey('activity_categories.id'), nullable=False)
        progress_id  = Column(String(60), ForeignKey('progress.id'), nullable=True)

        # Relationships
        progress = relationship("Progress", backref="student")
        activities = relationship("Activity", backref="student")
        badges = relationship("Badge", backref="Student")
        
    else:
        user_id = ""
        age = ""
        class_level = ""
        activityCategory_id = ""
        progress_id = ""
        stage = ""

    def __init__(self, *args, **kwargs):
        """initializes Profile"""
        super().__init__(*args, **kwargs)

