
import pickle #replace instead of json to store and load class object
import os  # for temporary files -->  replacing the files with temporary files
import difflib # for comparing text similiarity for search tasks // difflib = difference library // a module for comparing differences between text or sequences

#blueprint for the task
class Task:
    #constructor
    def __init__(self, name, priority):
        self.name = name
        self.status = False
        self.priority = priority
        
    #just normal function this blueprint will have
    def mark_done(self):
        self.status = True

    def mark_undone(self):
        self.status = False


tasks = [] # this is a list, rather than an array

#making this code into files
#load tasks from JSON file when program starts
#using JSON coz the simple txt file format can corrupt easily if it is manually edied from the files
try:
    with open("tasks.pkl", "rb") as file:
        tasks = pickle.load(file)
except:
    tasks = []

def view_tasks(tasks):
    for i, task in enumerate(tasks): # u must first show the list for them to choose
        name = task.name
        status = task.status
        priority = task.priority

        if task.status: # this syntax is the same with if status == True, for true u don't need to add == True. But if u want u can add that too.
            print(f"{i+1}. ✔ {name}\t{priority}")
        else:
            print(f"{i+1}. x {name}\t{priority}")

    show_progress(tasks)

def show_progress(tasks):
    total = len(tasks) #checking the total number of tasks
    done_count = 0

    for task in tasks:
        if task.status: # if task[1], which is status, == True
            done_count += 1

    print(f"{done_count} out of {total} tasks completed")

def view_completed(tasks):
    if len(tasks) == 0:
        print("No tasks yet.") # this is for checking if there are any tasks, not for checking any finsihed tasks
    else:
        found = False # this found var is for what happen when there is no finished tasks yet.
        count = 0

        for task in tasks:
            if task.status == True:
                count += 1
                print(f"{count}. {task.name}\t{task.priority}")
                found = True

        if not found: # if found == False:
            print("No completd tasks yet.")
    show_progress(tasks)

def view_unfinished(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        found = False
        count = 0

        for task in tasks:
            if task.status == False:
                count += 1
                print(f"{count}. {task.name}\t{task.priority}")
                found = True

        if not found:
            print("All tasks are done!")

    total = len(tasks) #checking the total number of tasks
    undone_count = 0

    for task in tasks:
        if task.status == False:
            undone_count += 1

    print(f"{undone_count} out of {total} tasks are still unfinished")

def view_priority(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print()
        print ("High priority tasks:")

        found = False
        count = 0

        for task in tasks:
            if task.priority == "high":
                count += 1

                status = task.status
                if status:
                    print(f"{count}.  ✔ {task.name}")
                else:
                    print(f"{count}. x {task.name}")

                found = True

        if not found:
            print("There is no high priority task.")

        print() # adding a blank line
        print ("Medium priority tasks:")

        found = False
        count = 0

        for task in tasks:
            if task.priority == "medium":
                count += 1

                status = task.status
                if status:
                    print(f"{count}.  ✔ {task.name}")
                else:
                    print(f"{count}. x {task.name}")

                found = True

        if not found:
            print("There is no medium priority task.")

        print()
        print ("Low priority tasks:")
        found = False
        count = 0

        for task in tasks:
            if task.priority == "low":
                count += 1

                status = task.status
                if status:
                    print(f"{count}.  ✔ {task.name}")
                else:
                    print(f"{count}. x {task.name}")

                found = True

        if not found:
            print("There is no low priority task.")

def add_task(tasks):
    while True:
        task_name = input("Enter task: ").strip()

        if task_name == "":
            print("Task name can't be blank.")
        else:
            break  # Input is valid, exit the loop
    while True:
        priority = input("Priority (low/medium/high): ").lower() # asking input for the priority from the user

        # making sure that the user doesn't input random thing except low, medium, and high // input validation
        if priority in ["low", "medium", "high"]:
            new_task = Task(task_name, priority)
            tasks.append(new_task)
            print("Task added!")
            break
        else:
            print("Invalid priority. Please type low, medium, or high.")

def edit_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Which task number to edit? ")) - 1
        #this will be the no user choose
        #to readjust the i+1 above
    except:
        print("Invalid input")
        return #
        # originally it was continue so that it will skip everything below and go back to the top of the loop (menu)
        # however, now that it is a separate function and no longer under the while menu loop,
        # continue won't work, thus, change to return

        # need to add try except error handling here coz, if there is no error handling here,
        # and the user added sth other int, then the program will crash without any notice
        # by adding try except, after invalid input, the program will go back to the main menu, not crash

    if 0 <= index < len(tasks): # index, the no the user choose should be > or = 0 and less than the length of the array
        new_task = input("Enter new task: ")
        tasks[index].name = new_task

        print("Task updated!")
        print("To change status, use 'Mark as done/undone' option.")
        print("To change priority, use 'Edit priority' option.")
    else:
        print("Invalid input")

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        view_tasks(tasks)# user needs to see the list first to decide which no to remove

            # just asking for input here, need to remind the user that they must add spaces between tasks
        user_input = input("Enter the task numbers you want to remove separated by SPACES (e.g., 1 5 16), or type q to cancel: ")

        if user_input.lower().strip() == "q":
            print("Deletion canceled.")
            return
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
                    print(f"Task number {task} does not exist.")

            except ValueError:
                print("Invalid input.")

            # sort in revesre and deleting
        if len(indexes_to_delete) > 0:
            indexes_to_delete.sort(reverse = True)
            for index in indexes_to_delete:
                tasks.pop(index)
                print("Task removed!")

def mark_done(tasks):

    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        view_tasks(tasks)

        user_input = input("Enter task numbers to mark as DONE separated by SPACES (e.g., 1 5 16), or type q to cancel: ")

        if user_input.lower().strip() == "q":
            print("Mark as done is canceled.")
            return

        tasks_to_mark = user_input.split()
        indexes_to_mark = []

        for task in tasks_to_mark:
            try:
                index = int(task) - 1

                if 0 <= index < len(tasks):
                    if index not in indexes_to_mark:
                        indexes_to_mark.append(index)
                else:
                    print(f"Task number {task} does not exist.")
            except ValueError:
                print(f"'{task}' is not a valid task number.")

            # Update the status
        if len(indexes_to_mark) > 0:
            for index in indexes_to_mark:
                tasks[index].mark_done()
            print("Selected tasks marked as completed!")
        else:
            print("No tasks were changed.")

def mark_undone(tasks):

    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        view_tasks(tasks)

        user_input = input("Enter task numbers to mark as UNDONE separated by SPACES (e.g., 1 5 16), or type q to cancel: ")

        if user_input.lower().strip() == "q":
            print("Mark is undone is canceled.")
            return

        tasks_to_mark = user_input.split()
        indexes_to_mark = []

        for task in tasks_to_mark:
            try:
                index = int(task) - 1

                if 0 <= index < len(tasks):
                    if index not in indexes_to_mark:
                        indexes_to_mark.append(index)
                else:
                    print(f"Task number {task} does not exist.")
            except ValueError:
                print(f"'{task}' is not a valid task number.")

            # Update the status
        if len(indexes_to_mark) > 0:
            for index in indexes_to_mark:
                tasks[index].mark_undone()
            print("Selected tasks marked as unfinished!")
        else:
            print("No tasks were changed.")

def edit_priority(tasks):

    view_tasks(tasks) # u must first show the list for them to choose

    try:
        index = int(input("Which task number's priority do you want to edit? ")) - 1
            #this will be the no user choose
            #to readjust the i+1 above
    except:
        print("Invalid input")
        return

    if 0 <= index < len(tasks):
        while True:
            tasks[index].priority = input("Priority (low/medium/high): ").lower() # asking input for the priority from the user

                # making sure that the user doesn't input random thing except low, medium, and high // input validation
            if tasks[index].priority in ["low", "medium", "high"]:
                print("Priority changed successfully!")
                break
            else:
                print("Invalid priority. Please type low, medium, or high.")

def search_task(tasks):
    keyword = input("Enter task name to search: ").lower()
        #.lower() to fix case sensitivity

    found = False
    match_count = 0

    for task in tasks:
        words = task.name.lower().split() # spliting the to feed the cat into "to, feed, the, cat" to make word to word fuzzy search

        matches = difflib.get_close_matches (keyword, words, n = 3, cutoff = 0.6)

        if matches:
            status = "✔" if task.status else "x"
            print(f"{status} {task.name}")
            found = True
            match_count += 1

    print(f"\n{match_count} out of {len(tasks)} tasks matched your input.")

    if not found:
        print("No close matches found.")



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
        add_task(tasks)

    # view task
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            view_tasks(tasks)

  # view only finished task
    elif choice == "3":
        view_completed(tasks)

    # view only unfinished task
    elif choice == "4":
        view_unfinished(tasks)

    # view tasks by priority
    elif choice == "5":
        view_priority(tasks)

    # edit task
    elif choice == "6":
        edit_task(tasks)

    # remove task
    elif choice == "7":
        remove_task(tasks)

    # mark as done
    elif choice == "8":
        mark_done(tasks)

    # mark as undone
    elif choice == "9":
        mark_undone(tasks)

    # edit priority
    elif choice == "10":
        edit_priority(tasks)

    # search/filter tasks
    elif choice == "11":
        search_task(tasks)

        # exit
    elif choice == "0":
        break

    else:
        print("Invalid input")



# save tasks to JSON file when program closes
with open("tasks_tmp.pkl", "wb") as file:
    pickle.dump(tasks, file)

# save edited tasks to the temporary file first
os.replace("tasks_tmp.pkl", "tasks.pkl")
print("Goodbye!")
