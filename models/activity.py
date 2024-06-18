#!/usr/bin/python3
""" Activity Module for EL project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.progress import Progress
from models.badge import Badge

class Activity(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = 'activities'
        category_id = Column(String(60), ForeignKey('activity_categories.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        student_id = Column(String(60), ForeignKey('student.id'), nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(256))
        icon_url = Column(String(256))

        # Relationships
        progress = relationship("Progress", backref="activities")
        badges = relationship("Badge", backref="activities")
    else:
        category_id = ""
        title = ""
        description = ""
        icon_url = ""
        user_id = ""
        student_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Activity"""
        super().__init__(*args, **kwargs)
