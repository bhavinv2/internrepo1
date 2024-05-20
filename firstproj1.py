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

