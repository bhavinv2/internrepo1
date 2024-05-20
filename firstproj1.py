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

