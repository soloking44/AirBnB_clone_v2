#!/usr/bin/python3
"""
this is the file storage
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """this is an instance of JSON code"""

    __file_path = "file.json"
  
    __objects = {}

    def fun(self, nes=None):
        """thia outputs dictionary __objects"""
        if nes is not None:
            res = {}
            for key, value in self.__objects.items():
                if nes == value.__class__ or nes == value.__class__.__name__:
                    res[key] = value
            return res
        return self.__objects

    def fun2(self, ptr):
        """this is the__objects the object"""
        if ptr is not None:
            key = ptr.__class__.__name__ + "." + ptr.id
            self.__objects[key] = ptr

    def fun3(self):
        """this is the JSON file""
        respo = {}
        for key in self.__objects:
            respo[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as files:
            json.dump(json_objects, files)

    def fun4(self):
        """this is the JSON"""
        try:
            with open(self.__file_path, 'r') as files:
                ryt = json.load(files)
            for key in ryt:
                self.__objects[key] = classes[ryt[key]["__class__"]](**ryt[key])
        except:
            pass

    def fun4(self, ptrs=None):
        """this removes ptrs"""
        if ptrs is not None:
            key = ptrs.__class__.__name__ + '.' + ptrs.id
            if key in self.__objects:
                del self.__objects[key]

    def fun5(self):
        """this intialize call reload()"""
        self.reload()
