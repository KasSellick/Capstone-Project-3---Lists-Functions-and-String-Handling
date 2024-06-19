def menu_options(logged_in_user):
    '''Display menu options to user.'''
    #Options for admin
    if logged_in_user == "admin":
      print('''\nPlease select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''')

    #Options for all other users
    else:
      print('''\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''')
    #Menu selection from user
    menu = input("").lower()

    return(menu)