greeting = """To start a conversation with Bot, you must enter one of the following commands:
          Hello - say "Hello"
          Add - add a name and number
          Change - change the phone number of an existing user
          Phone - show the phone number of an existing user
          Show all - show phonebook
          Close or Exit - exit"""

COMMANDS = ('hello', 'add', 'change', 'phone', 'show all', 'exit', 'close', 'good bye')

phonebook = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Please, enter Username and phone number'
        except KeyError:
            return 'The user does not exist...'
    return inner
        
def hello_command():
    return 'How can I help you?'

@input_error
def add_command(data):
    splitted_data = data.split()
    name = splitted_data[1]
    phone = splitted_data[2]
    phonebook[name] = phone
    return f'{name} with phone number {phone} was added to the phonebook'

@input_error
def change_command(data):
    splitted_data = data.split()
    name = splitted_data[1]
    phone = splitted_data[2]
    if phonebook[name]:
        phonebook[name] = phone
        return f'Phone number for user {name} was changed to {phone}'

@input_error
def show_phone(data):
    splitted_data = data.split()
    name = splitted_data[1]
    return f'Phone number for user {name} is {phonebook[name]}'

def show_all_command(data):
    if data == {}:
        return 'empty'
    else:
        user_and_phones_list = ['|{:^10}|{:^12}|'.format('Username', 'Phone number')]
        for user, phone in data.items():
            user_and_phones_list.append('|{:<10}|{:<12}|'.format(user, phone))
        return user_and_phones_list

def parser(command):
    cased_command = str(command.casefold())
    first_word = cased_command.split()

    if cased_command in ('good bye', 'close', 'exit'):
        return 'exit'
    
    if cased_command.startswith('show all'):
        return show_all_command(phonebook)

    if (first_word[0] not in COMMANDS):
        return 'Wrong command...'
    
    if cased_command.startswith('hello'):
        return hello_command()
    
    if cased_command.startswith('add'):
        return add_command(command)
    
    if cased_command.startswith('change'):
        return change_command(command)
    
    if cased_command.startswith('phone'):
        return show_phone(command)
    
def main():
    print(greeting)
    while True:
        users_input = input('Please, enter the command: ')
        result = parser(users_input)
        if result == 'exit':
            print('Good Bye!')
            break

        elif result == 'empty':
            print('Phone book is empty yet, please add username and phone number')
        elif isinstance(result, list):
            for el in show_all_command(phonebook):
                print(el)
        else:
            print(result)
        
main()