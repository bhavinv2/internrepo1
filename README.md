# Task Manager

## Overview

The Task Manager is a simple console-based application designed to help you manage tasks efficiently. It supports adding, viewing, editing, deleting, searching, and undoing tasks. Tasks can be tagged for easy searching, and all tasks are saved to a file for persistence between sessions.

## Features

- **Add Tasks**: Add new tasks with tags.
- **View Tasks**: View all tasks in a list.
- **Edit Tasks**: Edit existing tasks by specifying the task number.
- **Delete Tasks**: Delete tasks by specifying the task number.
- **Search Tasks**: Search for tasks by tags.
- **Undo Actions**: Undo the last action performed.
- **Persistent Storage**: Tasks are saved to a JSON file to retain data between sessions.

## Components

### LinkedList

A singly linked list implementation for managing tasks.

- **Node Class**: Represents a single node in the linked list.
- **LinkedList Class**: Manages the linked list with methods to add, delete, edit, and traverse nodes.

### Stack

A stack implementation used for undo functionality.

- **Stack Class**: Provides push, pop, and is_empty methods.

### HashTable

A hash table implementation for tagging and searching tasks.

- **HashTable Class**: Manages a dictionary to store tasks by tags.

### TaskManager

The main class that integrates LinkedList, Stack, and HashTable to manage tasks.

- **add_task**: Adds a task with a tag.
- **view_tasks**: Displays all tasks.
- **edit_task**: Edits a specified task.
- **delete_task**: Deletes a specified task.
- **search_task**: Searches for tasks by tag.
- **undo**: Undoes the last action.
- **save_tasks**: Saves tasks to a JSON file.
- **load_tasks**: Loads tasks from a JSON file.

### Controls

A function to manage user inputs and interactions with the TaskManager.

## How to Use

1. **Run the Program**: Execute the script in a Python environment.
2. **Follow Prompts**: The application will display a menu with options.
3. **Choose an Option**:
   - Press `1` to add a task.
   - Press `2` to view tasks.
   - Press `3` to edit a task.
   - Press `4` to delete a task.
   - Press `5` to search for tasks by tag.
   - Press `6` to undo the last action.
   - Press `7` to exit the program.

## Sample Interaction

Task Manager
- Press `1` to add a task.
- Press `2` to view tasks.
- Press `3` to edit a task.
- Press `4` to delete a task.
- Press `5` to search for tasks by tag.
- Press `6` to undo the last action.
- Press `7` to exit the program.
  
Choose a prompt: 1
- Enter a task: Complete project documentation
- Enter a tag: work
- Task added successfully.


## Requirements

- Python 3.x
- `json` module (standard library)

## File Structure

- `task_manager.py`: Main script file containing all classes and functions.
- `tasks.json`: File where tasks are stored.

## Notes

- Make sure to run the script in a directory where `tasks.json` can be created and accessed.
- Ensure Python 3.x is installed on your system.

---

This README provides a comprehensive guide to understanding, using, and extending the Task Manager application. Enjoy managing your tasks efficiently!
