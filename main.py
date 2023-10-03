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
def add_command(u_name, ph_number):
    phonebook[u_name] = ph_number
    return f'{u_name} with phone number {ph_number} was added to the phonebook'

@input_error
def change_command(u_name, ph_number):
    if phonebook[u_name]:
        phonebook[u_name] = ph_number
        return f'Phone number for user {u_name} was changed to {ph_number}'

@input_error
def show_phone(u_name):
    return f'Phone number for user {u_name} is {phonebook[u_name]}'

def show_all_command(data):
    if data == {}:
        return 'empty'
    else:
        user_and_phones_list = ['|{:^10}|{:^12}|'.format('Username', 'Phone number')]
        for user, phone in data.items():
            user_and_phones_list.append('|{:<10}|{:<12}|'.format(user, phone))
        return user_and_phones_list

@input_error
def parser(command):
    cased_command = str(command.casefold())
    splitted_string = cased_command.split()

    if cased_command in ('good bye', 'close', 'exit'):
        return 'exit'
    
    if cased_command.startswith('show all'):
        return show_all_command(phonebook)

    if (splitted_string[0] not in COMMANDS):
        return 'Wrong command...'
    
    if cased_command.startswith('hello'):
        return hello_command()
    
    if cased_command.startswith('add'):
        return add_command(splitted_string[1], splitted_string[2])
    
    if cased_command.startswith('change'):
        return change_command(splitted_string[1], splitted_string[2])
    
    if cased_command.startswith('phone'):
        return show_phone(splitted_string[1])
    
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

if __name__ == "__main__":        
    main()