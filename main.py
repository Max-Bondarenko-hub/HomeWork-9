greeting = """To start a conversation with Bot, you must enter one of the following commands:
          Hello - say "Hello"
          Add - add a name and number
          Change - change the phone number of an existing user
          Phone - show the phone number of an existing user
          Show all - show phonebook
          Close or Exit - exit"""

phonebook = {}

CMDS = {
    'hello': lambda *args: say_hello(),
    'add': lambda *args: add_command(*args),
    'change': lambda *args: change_command(*args),
    'phone': lambda *args: show_phone(*args),
    'show all': lambda *args: show_all_command(*args),
    'exit': lambda *args: say_goodbye(),
    'close': lambda *args: say_goodbye(),
    'good bye': lambda *args: say_goodbye()
}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Please, enter Username and phone number'
        except KeyError:
            return 'The user does not exist...'
        except TypeError:
            return 'Enter username to find phone number'
    return inner
        
def splitter(command_string):
    splitted = command_string.split()
    return splitted

def say_hello():
    return 'How can I help you?'

def say_goodbye():
    return 'exit'

@input_error
def add_command(*args):
    phonebook[args[0]] = args[1]
    return f'{args[0]} with phone number {args[1]} was added to the phonebook'

@input_error
def change_command(*args):
    if phonebook[args[0]]:
        phonebook[args[0]] = args[1]
        return f'Phone number for user {args[0]} was changed to {args[1]}'

@input_error
def show_phone(usr_name):
    return f'Phone number for user {usr_name} --> {phonebook[usr_name]}'

def show_all_command(*args):
    if phonebook == {}:
        return 'empty'
    else:
        user_and_phones_list = ['|{:^10}|{:^12}|'.format('Username', 'Phone number')]
        for user, phone in phonebook.items():
            user_and_phones_list.append('|{:<10}|{:<12}|'.format(user, phone))
        return user_and_phones_list

def parser(command: str):
    cased_command = str(command.casefold())

    for kw, func in CMDS.items():
        if cased_command.startswith(kw):
            data = command[len(kw):].strip().split()
            return func(*data)
    return 'Wrong command...'
    
def main():
    print(greeting)
    while True:
        users_input = input('Please, enter the command: ')
        result = parser(users_input)
        if result == 'exit':
            print('Good Bye!')
            break

        if result == 'empty':
            print('Phone book is empty yet, please add username and phone number')
        elif isinstance(result, list):
            for el in show_all_command(phonebook):
                print(el)
        else:
            print(result)

if __name__ == "__main__":        
    main()