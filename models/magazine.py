class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
         # If the input is not a string, it should raise an error
        if isinstance(new_name, str):
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        # If the input's length isn't between 2 and 16 chars, raise an error
            if len(new_name) >= 2 and len(new_name) <= 16:
                 self._name = new_name
            else:
                raise ValueError("name MUST be btn 2 and 16 characters")
        else:
            TypeError("name MUST be a string")
    
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        # If the input is not a string, it should raise an error
        if isinstance(new_category, str):
            # If the input is empty(less than one character) it should raise an error
            if len(new_category) > 0:
                 self._category = new_category
            else:
                raise ValueError("Please input a category")
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        else:
            TypeError("Category MUST be a string!!")
        