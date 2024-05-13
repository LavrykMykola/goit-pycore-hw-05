def input_error(func):  # Функція генератор для обробки помилок
    def wrapper(*args, **kwargs):  # Функція обгортка
        try:
            return func(*args, **kwargs)
        except ValueError: # Якщо введена не вірна кількість аргументів
            return "Please enter a name and a phone number"
        except Exception as e:  # Для обробки інших типів помилок
            return f"An error occurred: {e}"
    return wrapper


@input_error
def add_contact(args, contacts):  # Функція для додавання контактів
    name, phone = args
    if name in contacts:
        return 'Name already exists. Please choose a different name.'
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):  # Функція для зміни номера для існуючого контакту
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):  # Функція для виведення номеру телефону для існуючого контакту
    if len(args) == 1:  # Якщо аргумент один, продовжуємо код
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:  # Якщо аргумент не один, повертаємо помилку
        return "Please enter only an existing name."


@input_error
def delete_contact(args, contacts):
    if len(args) == 1:  # Якщо аргумент один, продовжуємо код
        name = args[0]
        if name in contacts:
            contacts.pop(name)
            return "Contact deleted."
        else:
            return "Contact not found."
    else:  # Якщо аргумент не один, повертаємо помилку
        return "Please enter only an existing name."


def parse_input(user_input):  # Функція для парсингу введеного користувачем рядка
    cmd, *args = user_input.split()  # Розділяємо рядок на команду і список аргументів
    cmd = cmd.strip().lower()  # Зводимо команду до нижнього регістру
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['exit', 'close']:
            print("Goodbye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'delete':
            print(delete_contact(args, contacts))
        elif command == 'all':
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
