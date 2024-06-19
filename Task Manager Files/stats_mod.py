from reports_mod import reports
import os.path

def stats():
    '''Display statistics contained in task_overview.txt and user_overview.txt.'''
    
    tasks_stats = 'task_overview.txt'
    users_stats = 'user_overview.txt'
    #check if files exist
    check_tasks_file = os.path.exists(tasks_stats)
    check_users_file = os.path.exists(users_stats)
    #generate files where necessary
    if check_tasks_file == False or check_users_file == False:
        reports()
    elif check_tasks_file == True and check_users_file == True:
        while True:
            generate = input("\nThe task and user report files already exist. Would you like to update these files? (Y/N): ")
            generate = generate.lower()
            if generate == 'y':
                reports()
                print("Reports have been updated.")
                break
            elif generate == 'n':
                break
            else:
                print("\nInvalid input. Please try again.")
    
    #printing statistics
    print("\n\033[1mTasks Overview:\033[0m\n")
    
    with open(tasks_stats,'r') as ts:
        for line in ts:
            print(line)
    
    print("\n\033[1mUsers Overview:\033[0m\n")
    
    with open(users_stats,'r') as us:
        for line in us:
            print(line)

