from Field import Field

class Phone(Field):
    # Constructor
    def __init__(self, phone_number):
        self.value = phone_number
    
    # Getter for value 
    @property
    def value(self):
        return self.value
    
    # Setter for value
    @value.setter
    def value(self, phone_number):
        self.value = phone_number

    # Object to str
    def __str__(self):
        return f"Phone number: {self.value}"