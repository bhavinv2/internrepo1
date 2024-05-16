# Add Tasks: Users should be able to add new tasks to the list.
# View Tasks: Users should be able to see all the tasks listed.
# Edit Tasks: Users should be able to modify the details of existing tasks.
# Delete Tasks: Users should be able to remove tasks from the list.

def banner():
    print ("Task manager")
    print("Press 1 to add tasks")
    print("Press 2 to view tasks")
    print("Press 3 to edit tasks")
    print("Press 4 to delete tasks")
    print("Press 5 to end program")


list_tasks=[]

def controls():
    while True:
        banner()
        user_input=int(input("enter a number:"))
        if user_input == 1:
            add_task = input("Enter a task:")
            add_task=str(add_task)
            list_tasks.append(add_task)


        elif user_input==2:
            print("Your tasks:")
            print(list_tasks)

        elif user_input == 3:
            print(list_tasks)
            edit_task=int(input("select the index number of which task you'd like to edit:"))
            print("You chose task:", list_tasks[edit_task])
            new_edit_task= input("Enter the task you want to replace this with:")
            list_tasks.remove(list_tasks[edit_task])
            list_tasks.insert(edit_task,new_edit_task)


        elif user_input == 4:
            print(list_tasks)
            delete_task=int(input("select the index number of which task you'd like to delete:"))
            list_tasks.remove(list_tasks[delete_task])


        elif user_input ==5:
            break



controls()





