'''Module containing functions to view and edit tasks of logged in user.

Functions:
  list_of_tasks(tasklist)
  task_editor(user_task_list,usernames)
  view_mine(logged_in_user,tasklist,usernames)
'''


from add_task_mod import due_date

def list_of_tasks(tasklist):
  '''Create a list of the tasks contained in tasks.txt'''
  tasks_list = []
  with open(tasklist, 'r') as tasks:
    for line in tasks:
      line_list_tasks = line.split(", ")
      line_list_tasks[5] = line_list_tasks[5].strip("\n")
      tasks_list.append(line_list_tasks)
  return(tasks_list)
    



def task_editor(user_task_list,usernames):
    '''Edit tasks of logged in user.'''
    task_editing = True
    while task_editing == True:
      #choose the task to edit
      while True:
        try:
          task_choice = int(input("\nPlease enter the number of the task you would like to edit or '0' to go back to the main menu:"))
          break
        except ValueError:
          print("\nInalid input. Please try again.")
      task_choice += -1 #-1 to get index number
      if task_choice in range(len(user_task_list)):
        edit_task_choice = user_task_list[task_choice]
        #check if task has been completed
        while True:
          task_completion_q = input("\nHave you completed this task? (Y/N): ")
          task_completion_q = task_completion_q.lower()
          if task_completion_q == 'y':
            edit_task_choice[5] = 'Yes'
            break
          elif task_completion_q == 'n':
            edit_task_choice[5] = 'No'
            break
          else:
            print("\nInvalid input. Please try again.")
        #if task not completed, allow editng
        if edit_task_choice[5] == 'No':
          while True:
            edit_choice = input(f"""\nPlease select one of the following options: 
              u - change username task is assigned to
              d - change due date of task
              e - exit editing this task\n""")
            edit_choice = edit_choice.lower()
            #edit user
            if edit_choice == 'u':
              while True:
                edit_task_choice[0] = input("\nPlease enter the username the task is assigned to: ")
                if edit_task_choice[0] in usernames:
                  break
                else:
                  print("\nThis user does not exist. Please try again.")
              user_task_list[task_choice] = edit_task_choice
            #edit due date
            elif edit_choice == 'd':
              edit_task_choice[4] = due_date()
              user_task_list[task_choice] = edit_task_choice
            #exit editing current task
            elif edit_choice == 'e':
              break
            else:
              print("\nInvalid input. Please try again.")
        #if task completed, cannot edit
        else:
          print("\nThis task has been completed. No edits can be made.")
      #exit editing   
      elif task_choice == -1:
        task_editing = False
      #invalid input
      else:
        print("\nInvalid input. Please try again.")
    return user_task_list
  





def view_mine(logged_in_user,tasklist,usernames):
    '''Display tasks of logged in user,
    allow editing through task_editor(user_task_list,usernames),
    rewrite tasks.txt with updated tasks.
    '''
    
    #create list of tasks
    tasks_list = list_of_tasks(tasklist)
    #empty list for user's tasks'
    user_task_list = []
    #to number each task of the user
    task_num = 1
    
    #print tasks of logged in user
    for task in tasks_list:
      if task[0] == logged_in_user:
        user_task_list.append(task) #add task to user's list'
        #separate task details for printing
        task_username = task[0]
        task_title = task[1]
        task_desc = task[2]
        task_assigned = task[3]
        task_due = task[4]
        task_completion = task[5]
        
        # Calculating the length of the longest value to align the text
        max_value_width = max(len(task_title), len(task_username), len(task_assigned), len(task_due), len(task_completion))
        # Print each line with labels and values aligned
        print("_"*50)
        print(f"\n\033[1mYour Task {task_num}\033[0m")
        print(f"\n\033[1m{'Task:':<20}\033[0m{task_title:<{max_value_width}}")
        print(f"\033[1m{'Assigned to:':<20}\033[0m{task_username:<{max_value_width}}")
        print(f"\033[1m{'Date assigned:':<20}\033[0m{task_assigned:<{max_value_width}}")
        print(f"\033[1m{'Due date:':<20}\033[0m{task_due:<{max_value_width}}")
        print(f"\033[1m{'Task Complete?':<20}\033[0m{task_completion:<{max_value_width}}")
        print(f"\033[1mTask description:\033[0m \n\t{task_desc}\n")
        print("_"*50)
        task_num += 1
      
    #updated user task list after editing  
    user_task_list_2 = task_editor(user_task_list,usernames)
    
    #update original task list with user's tasks
    for i in range(len(user_task_list_2)):
      index = tasks_list.index(user_task_list[i])
      tasks_list[index] = user_task_list_2[i]
    
    #write all tasks to tasks.txt
    with open(tasklist, 'w+') as tasks:
      for task in tasks_list[:-1]:
        task_string = ', '.join(task)
        task_string = task_string + '\n'
        tasks.write(task_string)
    #add last task without '\n'
    with open (tasklist, 'a+') as tasks:
      task_string = ', '.join(tasks_list[-1])
      tasks.write(task_string)
    
    return
