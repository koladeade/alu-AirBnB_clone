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

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__}] ({self.id}) {self.__dict__}"
        
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        iso_time = "%Y-%m-%dT%H:%M:%S.%f"
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.strftime(iso_time)
        rdict["updated_at"] = self.updated_at.strftime(iso_time)
        rdict["__class__"] = self.__class__.__name__
        return rdict
    