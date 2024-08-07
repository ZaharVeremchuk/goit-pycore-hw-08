from Field import Field
from datetime import datetime

class Birthday(Field):
    # Constructor
    def __init__(self, date: str):
        if datetime.strptime(date, "%d.%m.%Y"):
            self.value = date
        else:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    # Getter for value    
    @property
    def value(self) -> str:
        return self.value
    
    # Setter for value
    @value.setter
    def value(self, value) -> None:
        self.value = value
        
    