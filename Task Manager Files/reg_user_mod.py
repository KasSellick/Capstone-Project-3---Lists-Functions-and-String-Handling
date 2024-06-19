def reg_user(usernames,passwords,userlist):
    '''register a new user to users.txt'''

    new_user_check = False
    while new_user_check == False:
        new_username = input("\nPlease enter the new username you would like to register: ")
        if new_username in usernames: #check if user already exists
            print("\nThis username already exists. Please enter another username.")
        else:
            new_user_check = True
            usernames.append(new_username) #add username to usernames list
        #creating new password
        new_password = input("\nPlease enter a password for your new user: ")
        new_password_check = input("\nPlease confirm your password: ") #reenter password to verify
        while new_password != new_password_check: #checking if passwords match
            print("\nYour passwords do not match. Please try again.")
            new_password = input("\nPlease enter a password for your new user: ")
            new_password_check = input("\nPlease confirm your password: ")
        passwords.append(new_password) #add password to passwords list
        #adding new user login to user.txt
        new_user = f"\n{new_username}, {new_password}"
        with open(userlist, 'a+') as user:
            user.write(new_user)

    print("\nUser added successfully.")
    return