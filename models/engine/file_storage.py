#!/usr/bin/python3
"""This module defines a class to manage file storage for EL clone"""
import json
from models.activity import Activity
from models.base_model import BaseModel, Base
from models.badge import Badge
from models.activityCategory import ActivityCategory
from models.progress import Progress
from models.student import Student
from models.user import User


class FileStorage:
    """This class manages storage of EL models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.activity import Activity
        from models.base_model import BaseModel, Base
        from models.badge import Badge
        from models.activityCategory import ActivityCategory
        from models.progress import Progress
        from models.student import Student
        from models.user import User

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Activity': Activity,
                    'ActivityCategory': ActivityCategory, 'Badge': Badge, 'Student': Student,
                    'Progress': Progress
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
    
