def banner():
    print("Task Manager")
    print("Press 1 to add tasks")
    print("Press 2 to view tasks")
    print("Press 3 to edit tasks")
    print("Press 4 to delete tasks")
    print("Press 5 to end program")

def add_task(task_list):
    task = input("Enter a task: ")
    task_list.append(task)
    with open('data.txt', 'a') as file:
        file.write(task + '\n')
    print("Task added.")

def view_tasks(task_list):
    if task_list:
        print("Your tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}: {task}")
    else:
        print("No tasks to view.")

def edit_task(task_list):
    if task_list:
        view_tasks(task_list)
        try:
            task_number = int(input("Enter the number of the task to edit: "))
            if 1 <= task_number <= len(task_list):
                new_task = input("Enter new task to replace with: ")
                task_list[task_number - 1] = new_task
                with open('data.txt', 'w') as file:
                    for task in task_list:
                        file.write(task + '\n')
                print("Task edited")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to edit.")

def delete_task(task_list):
    if task_list:
        view_tasks(task_list)
        try:
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(task_list):
                task_list.pop(task_number - 1)
                with open('data.txt', 'w') as file:
                    for task in task_list:
                        file.write(task + '\n')
                print("Task deleted")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def controls():
    task_list = []
    try:
        with open('data.txt', 'r') as file:
            task_list = file.read().splitlines()
    except FileNotFoundError:
        pass

    while True:
        banner()
        try:
            user_input = int(input("Choose a prompt: "))
            if user_input == 1:
                add_task(task_list)
            elif user_input == 2:
                view_tasks(task_list)
            elif user_input == 3:
                edit_task(task_list)
            elif user_input == 4:
                delete_task(task_list)
            elif user_input == 5:
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")

controls()
