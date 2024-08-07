from Field import Field

class Name(Field):
    
    # Constructor
    def __init__(self, name):
        self.name = name

    # Getter for value
    @property
    def name(self):
        return self.name
    
    # Setter for value
    @name.setter
    def name(self, name):
        self.name = name