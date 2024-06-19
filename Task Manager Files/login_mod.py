'''Module containing functions needed to login user to task_manager.py.

Functions:
  usernames_passwords_list(userlist)
  username_login(usernames)
  password_login(usernames,passwords,logged_in_user)
'''


def usernames_passwords_list(userlist):
  '''Create lists of usernames and passwords contained in user.txt. Return usernames and passwords lists'''
  #Reading user.txt, separating usernames and passwords and adding relavant data to 'usernames' and 'passwords' lists
  usernames = []
  passwords = []
  with open(userlist, 'r+') as user:
    for line in user:
      line_list_user = line.split(", ")
      usernames.append(line_list_user[0])
      password = line_list_user[1]
      password = password.rstrip("\n") #to remove the 'new line' command from the password
      passwords.append(password)
  return usernames, passwords




def username_login(usernames):
  '''Check username for login.'''
  logged_in_user = ""
  user_check = False
  while user_check == False:
    login_user = input("\nPlease enter your username: ")
    if login_user in usernames:
      user_check = True
      logged_in_user = login_user
    else:
      print("\nThis username does not exist. Please try again.")
  return user_check,logged_in_user
  
  
  

def password_login(usernames,passwords,logged_in_user):
  '''Check password for login'''
  index = usernames.index(logged_in_user) #needed to match index of user to index of passwords
  pass_check = False
  while pass_check == False:
    login_pass = input("\nPlease enter your password: ")
    if login_pass in passwords[index]:
      pass_check = True
    else:
      print("\nIncorrect password. Please try again.")
  return pass_check