import json # for files 
import os  # for temporary files -->  replacing the files with temporary files
import difflib # for comparing text similiarity for search tasks

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
        priority = task[2]

        if status: # this syntax is the same with if status == True, for true u don't need to add == True. But if u want u can add that too.
            print(f"{i+1}. ✔ {name}\t{priority}")
        else:
            print(f"{i+1}. x {name}\t{priority}")

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
    print("5. View tasks by priority")
    print("6. Edit task")
    print("7. Remove task")
    print("8. Mark as done")
    print("9. Mark as undone")
    print("10. Edit priority")
    print("11. Search task")
    print("0. Exit")


    choice = input("Choose option: ")

    # add task
    if choice == "1":
         while True:
            task = input("Enter task: ").strip()

            if task == "":
                print("Task name can't be blank.")
            else:
                break  # Input is valid, exit the loop

         while True:
            priority = input("Priority (low/medium/high): ").lower() # asking input for the priority from the user

        # making sure that the user doesn't input random thing except low, medium, and high // input validation
            if priority in ["low", "medium", "high"]:
                tasks.append([task, False, priority])
                print("Task added!")
                break
            else:
                print("Invalid priority. Please type low, medium, or high.")


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
                    print(f"{count}. {task[0]}\t{task[2]}")
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
                    print(f"{count}. {task[0]}\t{task[2]}")
                    found = True

            if not found:
                print("All tasks are done!")

        total = len(tasks) #checking the total number of tasks
        undone_count = 0

        for task in tasks:
            if task[1] == False:
                undone_count += 1

        print(f"{undone_count} out of {total} tasks are still unfinished")

     # view tasks by priority
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print()
            print ("High priority tasks:")

            found = False
            count = 0

            for task in tasks:
                if task[2] == "high":
                    count += 1

                    status = task[1]
                    if status:
                        print(f"{count}.  ✔ {task[0]}")
                    else:
                        print(f"{count}. x {task[0]}")

                    found = True

            if not found:
                print("There is no high priority task.")

            print() # adding a blank line
            print ("Medium priority tasks:")

            found = False
            count = 0

            for task in tasks:
                if task[2] == "medium":
                    count += 1

                    status = task[1]
                    if status:
                        print(f"{count}.  ✔ {task[0]}")
                    else:
                        print(f"{count}. x {task[0]}")

                    found = True

            if not found:
                print("There is no medium priority task.")

            print()
            print ("Low priority tasks:")
            found = False
            count = 0

            for task in tasks:
                if task[2] == "low":
                    count += 1

                    status = task[1]
                    if status:
                        print(f"{count}.  ✔ {task[0]}")
                    else:
                        print(f"{count}. x {task[0]}")

                    found = True

            if not found:
                print("There is no low priority task.")


    # edit task
    elif choice == "6":
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
            print("To change priority, use 'Edit priority' option.")
        else:
            print("Invalid input")

    # remove task
    elif choice == "7":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
             view_tasks(tasks)# user needs to see the list first to decide which no to remove

            # just asking for input here, need to remind the user that they must add spaces between tasks
            user_input = input("Enter the task numbers you want to remove separated by SPACES (e.g., 1 5 16), or type q to cancel: ")

            if user_input.lower().strip() == "q":
                print("Deletion canceled.")
                continue # why continue --> coz by continue, everything below will be skipped and this will bring back to the while main menu loop
            # but if i write break here, the code end. it means the nearest loop got end. so the while main menu loop will end.

            # i need to add input validation here. but it is difficult to make input validation with if else here.
            # u will have to check if the code is 1,2,3 or 1,2, hello or just random words etc
            # there are too many possibility for the error and too many things to check
            # thus, we are gonna use try except here. Let's the user input things. and then check if those inputs are workable.


            tasks_to_delete = user_input.split() # tasks_to_delete is a list. but it will be list of strings.

            indexes_to_delete = [] # creating an empty list for real math numbers list.

            for task in tasks_to_delete:
                try:
                    index = int(task)-1

                    # checking the number the user type is in the tasks list
                    if 0 <= index < len(tasks):
                        indexes_to_delete.append(index) # adding the tasks no that are to be deleted. not yet deleting anything
                    else:
                        print(f"Task number {task} does not exist. Skipping it.")
                except ValueError:
                    print("Invalid input.")

            # sort in revesre and deleting
            if len(indexes_to_delete) > 0:
                indexes_to_delete.sort(reverse = True)
                    for index in indexes_to_delete:
                        tasks.pop(index)
                        print("Task removed!")


                
    
    # mark as done
    elif choice == "8":
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
    elif choice == "9":
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

    
    # edit priority
     elif choice == "10":
        view_tasks(tasks) # u must first show the list for them to choose

        try:
            index = int(input("Which task number's priority do you want to edit? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
        except:
            print("Invalid input")
            continue

        if 0 <= index < len(tasks):
            while True:
                tasks[index][2] = input("Priority (low/medium/high): ").lower() # asking input for the priority from the user

                # making sure that the user doesn't input random thing except low, medium, and high // input validation
                if tasks[index][2] in ["low", "medium", "high"]:
                    print("Priority changed successfully!")
                    break
                else:
                    print("Invalid priority. Please type low, medium, or high.")
                    

    # search/filter tasks
     elif choice == "11":
        keyword = input("Enter task name to search: ").lower()
        #.lower() to fix case sensitivity

        found = False
        match_count = 0

        for task in tasks:
            words = task[0].lower().split() # spliting the to feed the cat into "to, feed, the, cat" to make word to word fuzzy search

            matches = difflib.get_close_matches (keyword, words, n = 3, cutoff = 0.6)

            if matches:
                status = "✔" if task[1] else "x"
                print(f"{status} {task[0]}")
                found = True
                match_count += 1

        print(f"\n{match_count} out of {len(tasks)} tasks matched your input.")

        if not found:
            print("No close matches found.")
    
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
