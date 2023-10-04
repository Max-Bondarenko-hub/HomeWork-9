greeting = """To start a conversation with Bot, you must enter one of the following commands:
          Hello - say "Hello"
          Add - add a name and number
          Change - change the phone number of an existing user
          Phone - show the phone number of an existing user
          Show all - show phonebook
          Close or Exit - exit"""

phonebook = {}

CMDS = {
    'hello': lambda _: 'How can I help you?',
    'add': lambda command_line: add_command(command_line),
    'change': lambda command_line: change_command(command_line),
    'phone': lambda command_line: show_phone(command_line),
    'show all': lambda phonebook: show_all_command(phonebook) 
}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Please, enter Username and phone number'
        except KeyError:
            return 'The user does not exist...'
    return inner
        
def splitter(command_string):
    splitted = command_string.split()
    return splitted

@input_error
def add_command(command_line):
    splitted = splitter(command_line)
    phonebook[splitted[1]] = splitted[2]
    return f'{splitted[1]} with phone number {splitted[2]} was added to the phonebook'

@input_error
def change_command(command_line):
    splitted = splitter(command_line)
    if phonebook[splitted[1]]:
        phonebook[splitted[1]] = splitted[2]
        return f'Phone number for user {splitted[1]} was changed to {splitted[2]}'

@input_error
def show_phone(command_line):
    splitted = splitter(command_line)
    return f'Phone number for user {splitted[1]} is {phonebook[splitted[1]]}'

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
    splitted_string = splitter(cased_command)

    if command == 'show all':
        return CMDS[command](phonebook)

    for cmd in CMDS.keys():
        if cmd == splitted_string[0]:
            return CMDS[cmd](command)
    
    return 'Wrong command...'
    
def main():
    print(greeting)
    while True:
        users_input = input('Please, enter the command: ')
        if users_input in ('good bye', 'close', 'exit'):
            print('Good Bye!')
            break

        result = parser(users_input)

        if result == 'empty':
            print('Phone book is empty yet, please add username and phone number')
        elif isinstance(result, list):
            for el in show_all_command(phonebook):
                print(el)
        else:
            print(result)

if __name__ == "__main__":        
    main()