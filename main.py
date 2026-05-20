import json #for files 
import os  # for temporary files -->  replacing the files with temporary files


tasks = [] # this is a list, rather than an array

#making this code into files
#load tasks from JSON file when program starts
#using JSON coz the simple txt file format can corrupt easily if it is manually edied from the files
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []

def view_tasks(tasks):
    for i, task in enumerate(tasks): # u must first show the list for them to choose
        name = task[0]
        status = task[1]

        if status: # this syntax is the same with if status == True, for true u don't need to add == True. But if u want u can add that too.
            print(f"{i+1}. ✔ {name}")
        else:
            print(f"{i+1}. x {name}")

    show_progress(tasks)

def show_progress(tasks):
    total = len(tasks) #checking the total number of tasks
    done_count = 0

    for task in tasks:
        if task[1]: # if task[1], which is status, == True
            done_count += 1

    print(f"{done_count} out of {total} tasks completed")

# main menu
while True:
    print("\n--- TODO MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. View only completed tasks")
    print("4. View only unfinished tasks")
    print("5. Edit task")
    print("6. Remove task")
    print("7. Mark as done")
    print("8. Mark as undone")
    print("9. Search task")
    print("0. Exit")


    choice = input("Choose option: ")

    # add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append([task, False])
        print("Task added!")

    # view task
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            view_tasks(tasks)

  # view only finished task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.") # this is for checking if there are any tasks, not for checking any finsihed tasks
        else:
            found = False # this found var is for what happen when there is no finished tasks yet.
            count = 0

            for task in tasks:
                if task[1] == True:
                    count += 1
                    print(f"{count}. {task[0]}")
                    found = True

            if not found:
                print("No completd tasks yet.")
        show_progress(tasks)

    # view only unfinished task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            found = False
            count = 0

            for task in tasks:
                if task[1] == False:
                    count += 1
                    print(f"{count}. {task[0]}")
                    found = True

            if not found:
                print("All tasks are done!")

        total = len(tasks) #checking the total number of tasks
        undone_count = 0

        for task in tasks:
            if task[1] == False:
                undone_count += 1

        print(f"{undone_count} out of {total} tasks are still unfinished")


    # edit task
    elif choice == "5":
        view_tasks(tasks)

        try:
            index = int(input("Which task number to edit? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
        except:
            print("Invalid input")
            continue # skip everything below and go back to the top of the loop (menu)

        # need to add try except error handling here coz, if there is no error handling here,
        # and the user added sth other int, then the program will crash without any notice
        # by adding try except, after invalid input, the program will go back to the main menu, not crash

        if 0 <= index < len(tasks): # index, the no the user choose should be > or = 0 and less than the length of the array
            new_task = input("Enter new task: ")
            tasks[index][0] = new_task

            print("Task updated!")
            print("To change status, use 'Mark as done/undone' option.")

        else:
            print("Invalid input")

    # remove task
    elif choice == "6":

        view_tasks(tasks)# user needs to see the list first to decide which no to remove

        try:
            index = int(input("Which task number to remove? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
        except:
            print("Invalid input")
            continue

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task removed!")
        else:                           # i still need this part. coz this part is for the wrong number of tasks or handles valid integers outside task range,
            print("Invalid input")     # while the above try except one is for handling program crashs for input that are not integer or for the input that cannot be converted into integers
    
    
    # mark as done
    elif choice == "7":
        view_tasks(tasks) # u must first show the list for them to choose

        try:
            index = int(input("Which task number is done? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
        except:
            print("Invalid input")
            continue

        if 0 <= index < len(tasks):
            tasks[index][1] = True

    
    # mark as undone
    elif choice == "8":
        view_tasks(tasks) # u must first show the list for them to choose

        try:
            index = int(input("Which task number is undone? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
        except:
            print("Invalid input")
            continue

        if 0 <= index < len(tasks):
            tasks[index][1] = False
            # there should be error term

    
    # search/filter tasks
    elif choice == "9":
        keyword = input("Enter task name to search: ").lower()
        #.lower() so that the input is not case sensitive
        #.lower() is a method, not a function
        # method are essentially still a function but they are attached to an object
        # normally in funciton, we do print(variable)
        # in method, we do variable.lower()
        # it is like this funciton is part of/ extension of/ or belong to that variable (object/class)

        found = False
        match_count = 0

        for task in tasks:
            if keyword in task[0].lower():
                status = "✔" if task[1] else "x"
                print(f"{status} {task[0]}")
                found = True
                match_count += 1

        print(f"\n{match_count} out of {len(tasks)} tasks matched your input.")
        
    # exit
    elif choice == "0":
        break

    else:
        print("Invalid input")

# save tasks to temp JSON file first
with open("tasks_tmp.json", "w") as file:
    json.dump(tasks, file)

# save edited tasks to the json file when program closes
os.replace("tasks_tmp.json", "tasks.json")

###########################################################################################################################################

"""
notes on files

two layers
1. Memory (Python list)
2. File (saved data on disk)

Start program → LOAD file → tasks list
Run program → modify tasks list
Exit program → SAVE file → tasks.txt


///
but this way, if there is some errors while overwriting the old file and
saving it as new file, there can be file corruption.
So instead, do this.
first, when saving the new data, write it to temporary file.
only when the temporary file finished writing, save or overwrite the data to the old file (tasks.json)

import os
os.replace("tasks_tmp.json", "tasks.json")
"""
#######################################################
"""
this is nested list, not a dictionary --> need to upgrade to dic after this
tasks = [
    ["study", False],
    ["eat", True]
]

enumerate() --> let me loop through a list and automatically get the index (position) at the same time

 for i, task in enumerate(tasks): # u must first show the list for them to choose
        name = task[0]
        status = task[1]

        print(f"{i+1}. {name}- {status}")
here i am getting 1. 2 .3. according to the index number coz of enumerate() function.
if i just use
    for task in tasks:
this will just loop, without showing index number.


input() always give strings even if the user type the number
so if we want to have int we need to do it like this
    int(input())
"""
###########################################################
