class Field:
    # Constructor
    def __init__(self, field):
        self.value = field
    
    # Getter for value
    @property
    def value(self):
        return self.value
    
    # Setter for value
    @value.setter
    def value(self, value):
        self.value = value
    
    # Obj to str
    def __str__(self) -> str:
        return f"Field value: {self.value}"