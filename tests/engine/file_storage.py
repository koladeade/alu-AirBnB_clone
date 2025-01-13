#!/usr/bin/python3
"""
A file storage system for storing and retrieving objects to/from a son file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A file storage system for storing and retrieving objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently in storage.
        
        Returns:
        dict: A dictionary where keys are object identifiers and values
        are the corresponding objects.
        
        """

        return FileStorage.__objects

    def new(self, obj):

        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added to the storage.

        """
        
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
       
        """
        Saves the objects in the storage to the file specified in
        __file_path.

        The objects are serialized to a JSON string and written to the
        file. If the file does not exist, it will be created.

        If there is an error while writing to the file, the error is
        silently ignored.

        """
        
        rdict = {}

        for key, value in self.__objects.items():
            rdict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(rdict, file, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):

        """
        Reloads the objects in the storage from the file specified in
        __file_path.

        The objects are deserialized from the JSON string in the file and
        added to the storage. If the file does not exist, the storage is not
        modified.

        If there is an error while reading from the file, the error is
        silently ignored.

        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                rdict = json.load(file)

                for key, value in rdict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")

        except FileNotFoundError:
            pass
