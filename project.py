
def display_menu(): # function - displays some print upon launch
    print("===== To-Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task(tasks): # function - adds a new variable to our list 'tasks' - list defined later
    task = input("Enter task name: ") # task is the variable, which will be named the users input
    tasks.append(task) # adds our user input variable into our list
    print("Task added successfully!") # lets the user know input worked.

def view_tasks(tasks): # function - viewing our list variables.
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_task_done(tasks): # function - as described
    if not tasks: # detects if there are any variables(tasks) in our list
         print("No tasks to mark as done.") # if there isn't, will tell the user
         return # returns to baseline

    view_tasks(tasks) # display tasks with indicies 
    index = int(input("Enter task index to mark as done: ")) - 1

    if 0 <= index <len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")

def main(): # function - main program
    tasks = [] # empty list finally created

    while True:
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
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
