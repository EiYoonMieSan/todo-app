
import json #for files
import os  # for temporary files -->  replacing the files with temporary files
import difflib # for comparing text similiarity for search tasks // difflib = difference library // a module for comparing differences between text or sequences


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
        name = task["name"]
        status = task["status"]
        priority = task["priority"]

        if status: # this syntax is the same with if status == True, for true u don't need to add == True. But if u want u can add that too.
            print(f"{i+1}. ✔ {name}\t{priority}")
        else:
            print(f"{i+1}. x {name}\t{priority}")

    show_progress(tasks)

def show_progress(tasks):
    total = len(tasks) #checking the total number of tasks
    done_count = 0

    for task in tasks:
        if task["status"]: # if task[1], which is status, == True
            done_count += 1

    print(f"{done_count} out of {total} tasks completed")

def view_completed(tasks):
    if len(tasks) == 0:
        print("No tasks yet.") # this is for checking if there are any tasks, not for checking any finsihed tasks
    else:
        found = False # this found var is for what happen when there is no finished tasks yet.
        count = 0

        for task in tasks:
            if task["status"] == True:
                count += 1
                print(f"{count}. {task['name']}\t{task['priority']}")
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
            if task["status"] == False:
                count += 1
                print(f"{count}. {task['name']}\t{task['priority']}")
                found = True

        if not found:
            print("All tasks are done!")

    total = len(tasks) #checking the total number of tasks
    undone_count = 0

    for task in tasks:
        if task['status'] == False:
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
            if task["priority"] == "high":
                count += 1

                status = task["status"]
                if status:
                    print(f"{count}.  ✔ {task['name']}")
                else:
                    print(f"{count}. x {task['name']}")

                found = True

        if not found:
            print("There is no high priority task.")

        print() # adding a blank line
        print ("Medium priority tasks:")

        found = False
        count = 0

        for task in tasks:
            if task['priority'] == "medium":
                count += 1

                status = task["status"]
                if status:
                    print(f"{count}.  ✔ {task['name']}")
                else:
                    print(f"{count}. x {task['name']}")

                found = True

        if not found:
            print("There is no medium priority task.")

        print()
        print ("Low priority tasks:")
        found = False
        count = 0

        for task in tasks:
            if task["priority"] == "low":
                count += 1

                status = task["status"]
                if status:
                    print(f"{count}.  ✔ {task['name']}")
                else:
                    print(f"{count}. x {task['name']}")

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
            tasks.append({"name": task_name, "status": False, "priority": priority})
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
        tasks[index]["name"] = new_task

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
                tasks[index][1] = True
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
                tasks[index][1] = False
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
            tasks[index]["priority"] = input("Priority (low/medium/high): ").lower() # asking input for the priority from the user

                # making sure that the user doesn't input random thing except low, medium, and high // input validation
            if tasks[index]["priority"] in ["low", "medium", "high"]:
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
        words = task["name"].lower().split() # spliting the to feed the cat into "to, feed, the, cat" to make word to word fuzzy search

        matches = difflib.get_close_matches (keyword, words, n = 3, cutoff = 0.6)

        if matches:
            status = "✔" if task[1] else "x"
            print(f"{status} {task['name']}")
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
with open("tasks_tmp.json", "w") as file:
    json.dump(tasks, file)

# save edited tasks to the temporary file first
os.replace("tasks_tmp.json", "tasks.json")
print("Goodbye!")

##################################################################

"""
for search task
?? partial searching works. but need to study more on why the partial word also works. for example if i searhc paint. it also include paint and painting.

?? Can I import only parts of a module instead of the whole thing? --> yes (e.g. from math import sqrt)
?? When I import a module in Python, does the whole module get loaded into memory, or only the specific functions I use?
import math loads the whole module into memory once; Python doesn’t reload it again even if you use many functions.
from math import sqrt just gives you direct access to one function, but the module is still basically loaded anyway, so it’s more about convenience than memory saving.

?? what is the difference between a module and a class
module = file of reusable code
class = design
object = actual thing created from design
A module can CONTAIN classes.

"""
###################################################################

"""
notes on files

two layers
1. Memory (Python list)
2. File (saved data on disk)

Start program → LOAD file → tasks list
Run program → modify tasks list
Exit program → SAVE file → tasks.txt

with open("tasks_tmp.json", "w") as f:
    json.dump(tasks, f)

///
but this way, if there is some errors while overwriting the old file and
saving it as new file, there can be file corruption.
So instead, do this.
first, when saving the new data, write it to temporary file.
only when the temporary file finished writing, save or overwrite the data to the old file (tasks.json)

import os
os.replace("tasks_tmp.json", "tasks.json")
"""


"""
Json is just a raw text file, then why don't we just use the simple plain .txt file
--> coz simple .txt file are easy to corrupt.
--> json can corrupt too. but since it store with format, there is less chance to corrupt

however if the program grows, json won't be suitable anymore. it will become too slow.
this is where we upgrade to databases.


game files??
When you play a game like Pokémon, Minecraft, or Call of Duty, the game tracks hundreds of things at the exact same time: your health, your coordinates on the map, your inventory items, and your current quest progress.
When you hit "Save Game," the computer takes a snapshot of all those live numbers and freezes them into a file on your hard drive.
Games do not use JSON text files for this. They use Binary Files.
so it is simialr to the system restore point (on Windows) or a Snapshot / Time Machine (on macOS/Linux VMs).
or OS snapshot
"""


#########################################################
"""
****this is nested list, not a dictionary --> need to upgrade to dic after this
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
#############################################################

"""
when to use input validation and error handling (try except)?
input validation --> checking before the program used this data
like checking if the user input is correct usable number and not random words

try except --> after the program used this data, the data is not there, then the program crash, try except is used to prevent program crash
like the user type a valid number like 9, but the array only has 6 lists, then since 9 is not there in the program, the program crash
use try except in this scenario
"""


"""
error type of exception
four main types
1. ValueError --> wrong type of data error -- like converting hello into int
2. IndexError --> out of bounds error -- eg. happens when you try to grab sth from a list using a number that doesn't exist
3. TypeError --> mixing apples and organes error -- eg. happens when u try to combine two types of data like 5 + "apples"
4. ZeroDivisionError --> impossible math error -- happens when the code tries to divide a number by zero -- 10/0
"""

##############################################################

"""
Dictionary vs nested list
so the main benefit of dic is that the programmer no longer need to remember which index means which
eg. list --> task[2]
dic --> task["priority"]

big O notation
list --> O(n) linear time
If you want to find a task named "Buy Milk" in a list,
Python has to start at index 0 and check every single item one by one until it finds it.
If you have 1 million tasks, it might take 1 million checks.

dic --> O(1) constant time
ictionaries use a math trick called a Hash Table.
Python instantly calculates exactly where task["name"] is stored in your computer's memory.
Whether you have 4 tasks or 4 million tasks, finding a key takes exactly one step.

dic has O(1) coz it is basically a hash map. we just called it dic in python.

memory cost --> list use less memory than dic
Because lists are just simple, raw rows of data, they use less RAM.
Dictionaries require extra memory behind the scenes to build and maintain their hash tables.
it uses about 2 to 4 times more ram than a simple list.
however, for todo app, the memory difference is microscopic.
then when do the differnce become large --> when we use it in data science, ai, high volume networking. in short when it becomes big data.


if the taks list is small we can just add a note at the end
such as index 0 = name, index 1 = status. But the programmer needs to alwasy go back to the note which is torublesome
so it is a good practice to use dic if the memory differnce is not that much

also dic has built in .get(), whereas nested list doesn't and cannot use .get().
then, do we have .get() in dic list???? ----> no, because the outer container is still a list.
but once we loop throught the outer list and reach the inner dic, we can now use .get().
print(tasks[0].get("name"))  # Prints: Buy Milk
print(tasks[0].get("date", "No due date"))  # Prints: No due date

Why don't we have .get() in list?
Why? Because lists are ordered by index numbers (0, 1, 2...). Python's creators designed lists to be incredibly simple memory structures. If you ask for an index that isn't there, Python expects you to manage that boundary using length checks (len(my_list)), not a fallback method.

.get() in dictionary
The Old Way (dict[key]): This is aggressive. It tells Python: "Give me this key right now. If it's not there, crash the entire program."
The .get() Way (dict.get(key)): This is polite. It tells Python: "Please check if this key exists. If it does, give me its value. If it doesn't, just return None (or a default answer I choose) so we don't crash."
user = {"name": "Alice", "role": "Admin"}

# 1. Standard lookup (No fallback)
print(user.get("name"))     # Prints: Alice
print(user.get("age"))      # Prints: None (No crash!)

# 2. Lookup with a Custom Fallback Default
print(user.get("age", 25))  # Prints: 25 (Because "age" wasn't found)


in short, list only works with indexes, whereas the dic can work with name which make .get() avaiable

"""

"""
dictionary in python == hash map

hash function
how does it know which number to assign?
--> doesn't do randomly
--> use deterministic math

classic has function formula
Hash=(Previous Hash×31)+Byte Value of current letter

def manual_hash_function(key_string):
    hash_value = 0
    # 31 is a prime number that helps spread out the bits evenly
    prime_multiplier = 31

    for letter in key_string:
        # ord() converts a letter to its character number (e.g., 'B' = 66)
        letter_bytes = ord(letter)

        # The scrambling math formula
        hash_value = (hash_value * prime_multiplier) + letter_bytes

    return hash_value

# TEST THE MATH:
print(manual_hash_function("Buy Milk"))   # Always prints: 2043685973
print(manual_hash_function("Buy Milk"))   # Always prints: 2043685973
print(manual_hash_function("Go to Gym"))  # Always prints: 2244243673


2. does the cpu always use the remainder to figure out the index no or the memory address.
yes, almost alwasys. the cpu use the division method.

# Squeezing a huge hash number into an array of 8 slots
slot_index = 2043685973 % 8
print(slot_index) # Prints: 5 (Your data is stored in slot 5!)


ways to handle hash collision
1. linked list -
2. open addressing
"""

####################################################

"""
what is the benefits of using helper funciton if the code is small, like this to do list app?
--> coz it isolate blast radius
--> and it hanles variable scope, now all var no longer be a global var

isolate blast raidus means --> simply means we can narrow down where is the error and can fix it easier compared to the not isolating.
crash vs mistakes ???
crash --> A crash happens when you ask the computer to do something that is physically or mathematically impossible
according to the rules of the programming language. --> instantly shuts down the entire program
mistakes --> logically correct or not correct ?? --> it doesn't ask the computer to do sth that is impossible
but what it asks to do is sth that is not right
like instead of [index] - 1 it does [index]+1
the code still run
but the result is wrong
these miskake are also called logical bugs and they do not caused the program shut down but mess with the desired output


why vaiable linger in while loop ?
gloal/module scope -- inside the main script
local scope -- inside a funciton

"""




