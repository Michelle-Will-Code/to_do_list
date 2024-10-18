import sys
import os

class Task():

    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} : {status}"

class ToDoList():

    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def show_tasks(self):
        if self.tasks:
            print("Current tasks: \n")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks recorded.")

    def mark_complete(self, task):
        task.completed = True
        print(f"Task: '{task.description}' marked complete.")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # macOS and Linux

    # Fallback for IDEs
    sys.stdout.write("\033[2J\033[H") #clear screen, move cursor to top
    sys.stdout.flush()

#Main Program

def main():
    to_do_list = ToDoList()

    #sample data
    to_do_list.add_task("Finish assignment")
    to_do_list.add_task("Buy pumpkins")
    to_do_list.add_task("Buy concert tickets")

    main_screen_text = """
    Welcome to your To Do List

    what do you wish to do today?

    1. View Tasks
    2. Add Task
    3. Mark Task Complete
    4. See Previously Completed Tasks
    5. Exit app

    """

    print(main_screen_text)
    user_choice = input("    Make a choice and press Enter:")
    if user_choice == "1":
        clear_screen()
        to_do_list.show_tasks()

    elif user_choice == "2":
        new_task = input("Type in your new task: ")
        to_do_list.add_task(new_task)
        print(f"New task: ' {new_task} ' has been added.")
        to_do_list.show_tasks()

    elif user_choice == "3":
        find_task = input("Search task: ")
        found_task = [task for task in to_do_list.tasks if find_task.lower() in task.description.lower()]
        if found_task:
            for task in found_task:
                print(task)

            change = input("Do you wish to mark this item as complete? y/n")
            if change == "y":
                to_do_list.mark_complete(found_task[0])

            else:
                print("No changes made.")
        else:
            print("No matching tasks found.")


#calls main() to begin running app
main()