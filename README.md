TO-DO List CLI Application Documentation
Overview
This Python CLI application provides basic functionalities for managing a TO-DO list. It allows users to add, update, mark tasks as complete, remove tasks, and display tasks with optional sorting by priority. The application utilizes SQLite as the database for storing tasks.

Components
Main Script (todolist.py):

This is the main Python script that contains the TO-DO list application.
It uses the argparse module for command-line argument parsing and interacts with the SQLite database to perform various operations on tasks.
Database (tasks.db):

SQLite database file where the tasks and their details are stored.
The database has one table named tasks, which stores task information including task ID, task description, priority, and completion status.
Dependencies:

sqlite3: Python built-in library for working with SQLite databases.
argparse: Python built-in library for parsing command-line arguments.
tabulate: Third-party library for displaying data in tabular form.
Functionality
Adding a Task:

Users can add a new task with a description and an optional priority level.
Example command: python todolist.py add --task "Task description" --priority 2
Updating a Task:

Users can update the description of an existing task by specifying the task ID.
Example command: python todolist.py update --task_id 1 --task "Updated task description"
Marking a Task as Complete:

Users can mark a task as complete by specifying the task ID.
Example command: python todolist.py complete --task_id 1
Removing a Task:

Users can remove a task from the list by specifying the task ID.
Example command: python todolist.py remove --task_id 1
Displaying Tasks:

Users can view all tasks in the list, optionally sorted by priority.
Example command: python todolist.py show
Example command with sorting: python todolist.py show --sort_by_priority
Usage Instructions
Installation:

Make sure you have Python installed on your system.
Install the required dependencies using pip:
pip install tabulate
Running the Application:

Save the todo.py script and tasks.db database file in the same directory.
Open your terminal or command prompt.
Navigate to the directory where the script is saved.
Execute the desired commands to perform operations on the TO-DO list.
Command Syntax:

The general syntax for running the script is:
css

python todolist.py <action> [options]
Replace <action> with one of the following: add, update, complete, remove, show.
Specify appropriate options based on the action being performed.
Use --help option to display usage instructions and available options for each action.
Examples:

Adding a task:
csharp

python todolist.py add --task "Task description" --priority 2
Updating a task:
css

python todolist.py update --task_id 1 --task "Updated task description"
Marking a task as complete:
css

python todolist.py complete --task_id 1
Removing a task:
lua

python todolist.py remove --task_id 1
Displaying tasks:
sql

python todolist.py show
Displaying tasks sorted by priority:
sql

python todolist.py show --sort_by_priority
