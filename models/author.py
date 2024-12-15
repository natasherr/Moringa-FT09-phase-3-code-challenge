#Import the database
from database.connection import get_db_connection

class Author:
    all = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    # getter
    @property
    def id(self):
        return self._id
    
    # setter
    @id.setter
    def id(self, id):
        # The id must be of integer type
        if isinstance(id, int):
            self._id = id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, 'name'):
            raise AttributeError("Name cannot be changed after it has been instantiated!")
        else:
            if isinstance(new_name, str):
                # Name must be longer than 0 characters
                if len(new_name) > 0:
                    self._name = new_name


