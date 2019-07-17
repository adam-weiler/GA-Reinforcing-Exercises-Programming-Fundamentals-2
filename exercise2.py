names_list = ['Tom', 'Richard', 'Harry']

def get_user_name(): #Asks the user for their name.
    print('Please enter your username:')
    return input()


def check_user_name(): #Checks if the username is in the list of names.
    user_name = get_user_name()

    for name in names_list: #Iterates through the names in names_list.
        # print(name)

        if user_name == name: #If user_name is the same as current iteration name.
            return f'Hello, {name}!'

    return 'Who goes there!?' #Else user_name is not in the list.


print(check_user_name())