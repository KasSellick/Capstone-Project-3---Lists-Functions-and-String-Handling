'''Module to generate statistics of tasks and users.

Functions:
    stats_info(tasks_list,users_list)
    reports()
'''


from view_mine_mod import list_of_tasks
from login_mod import usernames_passwords_list
from datetime import datetime,date


users = 'user.txt'
tasks = 'tasks.txt'

#create lists of tasks and users
tasks_list = list_of_tasks(tasks)
users_list = usernames_passwords_list(users)[0]



def stats_info(tasks_list,users_list):
    '''Obtain statistics from tasks list and users list.'''
    num_users = len(users_list) 
    #counts needed for tasks stats
    num_tasks = 0
    not_completed_tasks = 0
    overdue_tasks = 0
    #empty list for user stats
    tasks_per_user = []
    
    #obtaining info for tasks stats
    for task in tasks_list:
        num_tasks += 1
        if task[5].strip("\n") == 'No':
            not_completed_tasks += 1
            due_date = task[4]
            due_date = datetime.strptime(due_date, '%d %b %Y')
            if due_date.date() < datetime.now().date():
                overdue_tasks += 1
    
    completed_tasks = num_tasks - not_completed_tasks
    not_completed_percentage = (not_completed_tasks/num_tasks)*100
    if not_completed_tasks > 0 and overdue_tasks > 0:
        overdue_percentage = (overdue_tasks/not_completed_tasks)*100
    else:
        overdue_percentage = 0
    #list of tasks info
    tasks_info = [num_tasks,completed_tasks,not_completed_tasks,overdue_tasks,not_completed_percentage,overdue_percentage]
    
    #obtaining info for users stats        
    for user in users_list:
        task_count_user = 0
        not_completed_user = 0
        overdue_user = 0
        for task in tasks_list:
            if task[0] == user:
                task_count_user +=1
                if task[5].strip("\n") == 'No':
                    not_completed_user += 1
                    due_date = task[4]
                    due_date = datetime.strptime(due_date, '%d %b %Y')
                    if due_date.date() < datetime.now().date():
                        overdue_user += 1
        user_task_total_percent = (task_count_user/num_tasks)*100
        if task_count_user > 0:
            user_completed_percentage = ((task_count_user - not_completed_user)/task_count_user)*100
            user_not_completed_percentage = (not_completed_user/task_count_user)*100
        else:
            user_completed_percentage = 0
            user_not_completed_percentage = 0
        if not_completed_user > 0:
            user_overdue_percentage = (overdue_user/not_completed_user)*100
        else:
            user_overdue_percentage = 0
        #adding each user's stats as a tuple to user stats list
        user_details = (user,task_count_user,user_task_total_percent,user_completed_percentage,user_not_completed_percentage,user_overdue_percentage)
        tasks_per_user.append(user_details)
    
    return tasks_info,tasks_per_user,num_users
            
    

def reports():
    '''Generate report files for task statistics and user statistics.'''
    #getting info from stats_info function
    tasks_info,tasks_per_user,num_users = stats_info(tasks_list,users_list)
    #writing file for tasks stats
    with open('task_overview.txt','w+') as to:
        to.write(f"""
        ________________________________________
        Total tasks: \t\t\t\t\t\t {tasks_info[0]}
        Total completed tasks: \t\t\t\t\t {tasks_info[1]}
        Total uncompleted tasks: \t\t\t\t {tasks_info[2]}
        Total uncompleted tasks that are overdue: \t\t {tasks_info[3]}
        Percentage of total tasks not completed: \t\t {tasks_info[4]}%
        Percentage of not completed tasks that are overdue: \t {tasks_info[5]}%
        ________________________________________
        """)
    
    #writing file for user stats
    with open('user_overview.txt','w+') as uo:
        uo.write(f"""
        Total users: \t\t {num_users}
        Total tasks: \t\t {tasks_info[0]}
        
        Information for each user:\n""")
        for info in tasks_per_user:
            uo.write(f"""
            ________________________________________
            Username: \t\t\t\t\t\t\t\t {info[0]}
            Total user tasks: \t\t\t\t\t\t\t {info[1]}
            Percentage of total tasks assigned to user: \t\t\t {info[2]}%
            Percentage of user's tasks that are completed: \t\t\t {info[3]}%
            Percentage of user's tasks that are not completed: \t\t\t {info[4]}%
            Percentage of user's uncompleted tasks that are overdue: \t\t {info[5]}%
            ________________________________________
            """)
    return
