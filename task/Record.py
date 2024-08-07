import re

class Record:
    # Constructor
    def __init__(self, name: str):
        self.name = name
        self.phones = []
        self.birthday = None

    # Obj to str
    def __str__(self):
        if self.birthday is None:
            return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
        else:
            return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}, birthday: {self.birthday}"
    
    # Add new phone number to record
    def add_phone(self, phone: str) -> None:
        if re.match("\d{10}", phone):
            self.phones.append(phone)
        else:
            print("Phone need to have 10")

    # Edit phone by name and old phone to new phone number 
    def edit_phone(self, old_phone: str, new_phone: str) -> str:
          for phone in self.phones:
                if phone == old_phone:
                    self.phones.remove(phone)  # Remove old number
                    self.phones.append(new_phone)  # Add new number

    # Find phone by number                  
    def find_phone(self, phone: str) -> str:
          for ph in self.phones:
                if ph == phone:
                    return phone
    
    # Remove phone by number
    def remove_phone(self, phone : str) -> None:
          for ph in self.phones:
                if ph == phone:
                      self.phones.remove(ph) 
    
    # Add birthday by number
    def add_birthday(self, birthday: str) -> str:
        self.birthday = birthday
        return "Birthday added"
        
            