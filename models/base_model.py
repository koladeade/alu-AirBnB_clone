#!/usr/bin/python3
#create the base model class with the following attributes:
#1. id.
#2. created_at.
#3. updated_at.
#4. __str__: should print: [<class name>] (<self.id>) <self.__dict__>
#5. and the following methods:
#6. to_dict return a dictionary containing all keys/values of __dict__ of the instance.
#created at and updated_at will be converted to string object in ISO format:
#format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
# you can use isoformat() of datetime object


from datetime import datetime
import uuid


class BaseModel:

    """This is the basemodel class"""

    def __init__(self, *args, **kwargs):
        

        
        """
        Initializes a new instance of the BaseModel class.

        If kwargs is not empty, it iterates over the dictionary and sets the
        attributes of the instance with the corresponding values from the
        dictionary. If the key is 'created_at' or 'updated_at', it converts the
        value to a datetime object using datetime.fromisoformat().

        If kwargs is empty, it sets the id to a new uuid, and the created_at and
        updated_at to the current datetime.

        It then calls new() in storage to save the instance into the storage.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        The string is in the format:
        [{class_name}] ({id}) {dict}
        Where class_name is the name of the class of the instance,
        id is the value of the id attribute of the instance,
        and dict is a string representation of the __dict__ of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
    def save(self):
        """
        Updates the attribute 'updated_at' with the current datetime.

        This method is mainly used to keep track of the last time an instance
        was modified. It should be called whenever the instance is changed.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all the attributes of the instance.

        The dictionary keys are the same as the attribute names of the instance,
        and the values are the corresponding attribute values.

        The keys 'created_at' and 'updated_at' are special, and contain the
        corresponding datetime objects converted to strings in ISO format:
        %Y-%m-%dT%H:%M:%S.%f

        The key '__class__' contains the name of the class of the instance as a
        string.

        The returned dictionary is a shallow copy of the __dict__ of the
        instance, so it will not be affected by changes to the instance's
        attributes after the call to to_dict.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        return rdict
