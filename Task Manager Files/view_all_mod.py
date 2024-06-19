def view_all(tasklist):
    '''print all tasks contained in tasks.txt'''

    #Reading tasks.txt, separating information in each task and printing information for each task
    with open(tasklist, 'r') as tasks:
        task_num = 1
        for line in tasks:
          line_list_tasks = line.split(", ")
          task_username = line_list_tasks[0]
          task_title = line_list_tasks[1]
          task_desc = line_list_tasks[2]
          task_assigned = line_list_tasks[3]
          task_due = line_list_tasks[4]
          task_completion = line_list_tasks[5]
          task_completion = task_completion.strip("\n")
          # Calculate the maximum width for the values to align the text
          max_value_width = max(len(task_title), len(task_username), len(task_assigned), len(task_due), len(task_completion))
          # Print information on separate lines with labels and values aligned
          print("_"*50)
          print(f"\n\033[1mTask {task_num}\033[0m")
          print(f"\n\033[1m{'Task:':<20}\033[0m{task_title:<{max_value_width}}")
          print(f"\033[1m{'Assigned to:':<20}\033[0m{task_username:<{max_value_width}}")
          print(f"\033[1m{'Date assigned:':<20}\033[0m{task_assigned:<{max_value_width}}")
          print(f"\033[1m{'Due date:':<20}\033[0m{task_due:<{max_value_width}}")
          print(f"\033[1m{'Task Complete?':<20}\033[0m{task_completion:<{max_value_width}}")
          print(f"\033[1mTask description:\033[0m \n\t{task_desc}\n")
          print("_"*50)
          task_num += 1
    return