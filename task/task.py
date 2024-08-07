
from functools import wraps # just for metadata of func
from AddressBook import AddressBook
from Record import Record
import pickle

# Decorator
def input_error(func):
    @wraps(func) # To get metadata of inner function in future
    def inner(*args, **kwargs):
        # Handle exception
        try:
            return func(*args, **kwargs)    # Call the func with arguments
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Please provide normal key"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Use decorator for func 
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

# Use decorator for func 
@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone ,*_ = args
    record = book.find(name)
    phone = record.find_phone(old_phone)
    if record is None:
        return "User with this name not found"
    if phone:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        return "Phone not found"

# Use decorator for func 
@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f'Name: {name}, phones: {record.phones}'
    return 'User doesn\'t exist'

# Use decorator for func 
@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_  = args
    record = book.find(name)
    if record:
        return record.add_birthday(birthday)
    return "User with this name not found"

# Use decorator for func 
@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return "User don't have any info about birthday"
    else:
        return "User with this name not found"

# Use decorator for func 
@input_error
def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
        print("Address book saved")

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("File with serialiazed Addressbook data not found")
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


    
# add john 1234567891
# change john 1234567891 1234567892
# add-birthday john 07.08.2023
# show-birthday john


def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "show":
            print(show_phone(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command == "all":
            print(book)
        else:
            print("Invalid command.")

    save_data(book)

if __name__ == "__main__":
    main()