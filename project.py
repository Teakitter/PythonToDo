# ------------------------
    # tasks = our list
    # task = task variable, stored in our tasks list
    # \n is a line break
    # w = opens a pre-existing file, creates a new one if it does not exist.
# ------------------------

def display_menu(): # function - displays some print upon launch
    print("-----------------------")
    print("       lots to do      ")
    print("-----------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task(tasks): # function - adds a new variable to our list 'tasks' - list defined later
    task = input("Enter task name: ") # task is the variable, which will be named the users input
    tasks.append(task) # adds our user input variable into our list
    print(f"Task '{task}' added successfully!") # lets the user know input worked. f allows for a variable to be used, and in this case our variable is {task}, which will be user input

def view_tasks(tasks): # function - viewing our list variables.
    print("\nTasks:") # \n creates a line break, then begins listing. 
    for i, task in enumerate(tasks, start=1): # clarification needed - i = index, then task name, enumerate means list one by one. right now, its taking all of tasks in our list and writing them out bbehind the scenes
        print(f"{i}. {task}") # then prints all of the tasks based on the above? f is inserting variables (in this case, the index and the task, then it follows the neumerate ) this line pritns out what above did.

def mark_task_done(tasks): # function - as described
    if not tasks: # detects if there are any variables(tasks) in our list
         print("No tasks to mark as done.") # if there isn't, will tell the user
         return # returns to baseline

    view_tasks(tasks) # display task function
    index = int(input("Enter task index to mark as done: ")) - 1

    if 0 <= index <len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.") #f is to allow input of which task
    else:
        print("Invalid task index.")

def save_tasks(tasks): # save tasks to a txt file for it to be presistent
    with open("tasks.txt", "w") as f: # opens our tasks text file, creates it if it does not exist. as f in the with open line means that the following (the f.write) is done with the text file?
        for task in tasks:
            f.write(task + '\n')

def load_tasks(tasks):
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def main(): # function - main program
    tasks = load_tasks()

    while True: # runs until told to stop
        display_menu() # while our function is active, display our menu function

        choice = input("Enter your choice: ") # detects user input, then runs the appropriate function based on input.

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()