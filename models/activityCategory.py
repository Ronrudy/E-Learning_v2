#!/usr/bin/python3
""" ActivityCategory Module for EL project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.progress import Progress
from models.activity import Activity


class ActivityCategory(BaseModel, Base):
    """Representation of activityCategory """
    if models.storage_t == 'db':
        __tablename__ = 'activity_categories'
        name = Column(String(60), nullable=False)
        description = Column(String(200))
        icon_url = Column(String(256))

        # Relationships
        activities = relationship("Activity", backref="activity_categories")
    else:
        name = ""
        description = ""
        icon_url = ""

    def __init__(self, *args, **kwargs):
        """initializes ActivityCategory"""
        super().__init__(*args, **kwargs)


    