'''Module containting functions to add a task to tasks.txt.

Functions:
    due_date()
    add_task(usernames,tasks)
'''

from datetime import datetime,date
 
def due_date(): #function adapted from https://python-forum.io/thread-35337.html
    '''Enter date string.  Return reformatted datestring and flag indicating if date is in the past'''
    while True: #check if input format is correct
        due = input('\nPlease enter the due date of the task in the format d/m/yyyy: ')
        try:
            due = datetime.strptime(due, '%d/%m/%Y')
        except ValueError:
            print("\nIncorrect date format. Please try again.")
        else: #check due date is not before assignment date
            if due.date() >= datetime.now().date():
                return due.strftime('%d %b %Y')
            print("\nDue date cannot be in the past. Please try again.")
  


def add_task(usernames,tasks):
    '''add a new task to tasks.txt'''

    #Check if a valid username has been used
    task_user_check = False
    while task_user_check == False:
        task_username_new = input("\nPlease enter the username of whom the task is assigned to: ")
        if task_username_new in usernames:
          task_user_check = True
        else:
          print("\nThis username does not exist. Please try again.")
    #Getting relevant information for task
    task_title_new = input("\nPlease enter the task title: ")
    task_desc_new = input("\nPlease enter the description of the task: ")
    task_assigned_new = date.today().strftime("%d %b %Y")
    task_due_new = due_date()
    task_completion_new = "No"
    #Adding task to tasks.txt
    task_total_new = f"\n{task_username_new}, {task_title_new}, {task_desc_new}, {task_assigned_new}, {task_due_new}, {task_completion_new}"
    with open(tasks, 'a+') as tasks:
        tasks.write(task_total_new)

    print("\nTask added successfully.")
    return 