class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if not current.next:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

    def edit(self, index, new_data):
        current = self.head
        for i in range(index):
            if not current.next:
                return
            current = current.next
        current.data = new_data

    def traverse(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

class HashTable:
    def __init__(self):
        self.table = {}

    def add(self, key, value):
        if key not in self.table:
            self.table[key] = []
        self.table[key].append(value)

    def search(self, key):
        return self.table.get(key, [])



import json

class TaskManager:
    def __init__(self):
        self.tasks = LinkedList()
        self.undo_stack = Stack()
        self.hash_table = HashTable()
        self.load_tasks()

    def save_tasks(self):
        tasks = self.tasks.traverse()
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
                for task in tasks:
                    self.tasks.add(task)
        except FileNotFoundError:
            pass

    def add_task(self, task, tag):
        self.tasks.add(task)
        self.hash_table.add(tag, task)
        self.undo_stack.push(("add", task, tag))
        self.save_tasks()

    def view_tasks(self):
        tasks = self.tasks.traverse()
        if tasks:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}: {task}")
        else:
            print("No tasks to view.")

    def edit_task(self, index, new_task, new_tag):
        old_task = self.tasks.traverse()[index - 1]
        self.tasks.edit(index - 1, new_task)
        self.undo_stack.push(("edit", index - 1, old_task, new_task, new_tag))
        self.save_tasks()

    def delete_task(self, index):
        task = self.tasks.traverse()[index - 1]
        self.tasks.delete(index - 1)
        self.undo_stack.push(("delete", index - 1, task))
        self.save_tasks()

    def search_task(self, tag):
        tasks = self.hash_table.search(tag)
        if tasks:
            print(f"Tasks with tag '{tag}':")
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found with tag '{tag}'.")

    def undo(self):
        if self.undo_stack.is_empty():
            print("No actions to undo.")
            return
        action = self.undo_stack.pop()
        if action[0] == "add":
            task = action[1]
            tag = action[2]
            self.tasks.delete(self.tasks.traverse().index(task))
            self.hash_table.table[tag].remove(task)
        elif action[0] == "edit":
            index, old_task, new_task, new_tag = action[1:]
            self.tasks.edit(index, old_task)
            self.hash_table.table[new_tag].remove(new_task)
        elif action[0] == "delete":
            index, task = action[1:]
            self.tasks.add(task)
        self.save_tasks()



def banner():
    print("Task Manager")
    print("Press 1 to add tasks")
    print("Press 2 to view tasks")
    print("Press 3 to edit tasks")
    print("Press 4 to delete tasks")
    print("Press 5 to search tasks")
    print("Press 6 to undo last action")
    print("Press 7 to end program")


def controls():
    task_manager = TaskManager()

    while True:
        banner()
        try:
            user_input = int(input("Choose a prompt: "))
            if user_input == 1:
                task = input("Enter a task: ")
                tag = input("Enter a tag: ")
                task_manager.add_task(task, tag)
                print("Task added successfully.")
            elif user_input == 2:
                task_manager.view_tasks()
            elif user_input == 3:
                task_manager.view_tasks()
                index = int(input("Enter the number of the task to edit: "))
                new_task = input("Enter new task to replace with: ")
                new_tag = input("Enter new tag: ")
                task_manager.edit_task(index, new_task, new_tag)
                print("Task edited successfully.")
            elif user_input == 4:
                task_manager.view_tasks()
                index = int(input("Enter the number of the task to delete: "))
                task_manager.delete_task(index)
                print("Task deleted successfully.")
            elif user_input == 5:
                tag = input("Enter a tag to search: ")
                task_manager.search_task(tag)
            elif user_input == 6:
                task_manager.undo()
                print("Last action undone.")
            elif user_input == 7:
                break
            else:
                print("Invalid option. Please choose a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")


controls()
