'''Program for a small business to help manage tasks assigned to each member of the team

The program asks the user to login and checks details against information in file user.txt.
A menu is displayed to the user with a list of options.
If the user is the admin, the menu options are:
  r - register a user
  a - add task
  va - view all tasks
  vm - view my tasks
  gr - generate reports
  ds - display statistics
  e - exit
The menu options for any other user are:
  a - add task
  va - view all tasks
  vm - view my tasks
  e - exit
  '''



#=====importing libraries

from login_mod import usernames_passwords_list, username_login, password_login
from menu_mod import menu_options
from reg_user_mod import reg_user
from add_task_mod import add_task
from view_all_mod import view_all
from view_mine_mod import view_mine
from stats_mod import stats
from reports_mod import reports

users = 'user.txt'
tasks = 'tasks.txt'

usernames,passwords = usernames_passwords_list(users)

#====Login Section====



user_check,logged_in_user = username_login(usernames)

pass_check = password_login(usernames,passwords,logged_in_user)

#====Menu====

#Printing menu options:
while user_check ==  True and pass_check == True:
    menu = menu_options(logged_in_user)

    #Register a new user (admin only)
    if menu == 'r' and logged_in_user == "admin":
      #creating new username
      reg_user(usernames,passwords,users)
      usernames,passwords = usernames_passwords_list(users)
      
    #Adding a task
    elif menu == 'a':
      add_task(usernames,tasks)
    
    #View all tasks
    elif menu == 'va':
      view_all(tasks)

    #View tasks of current logged in user
    elif menu == 'vm':
      view_mine(logged_in_user,tasks,usernames)

    elif menu == 'gr' and logged_in_user == "admin":
      reports()
      print("\nReports generated.")

    #Statistics of users and tasks (admin only)
    elif menu == 'ds'and logged_in_user == "admin":
      stats()

    #Exiting program
    elif menu == 'e':
        print('\nGoodbye!')
        exit()
        #break

    #Invalid input from user
    else:
        print("\nYou have entered an invalid input. Please try again.")
