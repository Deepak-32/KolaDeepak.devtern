import sqlite3
import argparse
from tabulate import tabulate

# Connect to the SQLite database
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT, priority INTEGER, completed BOOLEAN)''')

conn.commit()

def add_task(task, priority):
    c.execute("INSERT INTO tasks (task, priority, completed) VALUES (?, ?, ?)", (task, priority, False))
    conn.commit()

def update_task(task_id, new_task):
    c.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
    conn.commit()

def mark_as_complete(task_id):
    c.execute("UPDATE tasks SET completed=? WHERE id=?", (True, task_id))
    conn.commit()

def remove_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def show_tasks(sort_by_priority=False):
    if sort_by_priority:
        c.execute("SELECT * FROM tasks ORDER BY priority DESC")
    else:
        c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    headers = ['ID', 'Task', 'Priority', 'Completed']
    print(tabulate(tasks, headers=headers))

def main():
    parser = argparse.ArgumentParser(description='TO-DO List CLI')
    parser.add_argument('action', choices=['add', 'update', 'complete', 'remove', 'show'])
    parser.add_argument('--task_id', type=int, help='Task ID')
    parser.add_argument('--task', help='Task description')
    parser.add_argument('--priority', type=int, help='Task priority', default=1)
    parser.add_argument('--sort_by_priority', action='store_true', help='Sort tasks by priority')

    args = parser.parse_args()

    if args.action == 'add':
        add_task(args.task, args.priority)
    elif args.action == 'update':
        update_task(args.task_id, args.task)
    elif args.action == 'complete':
        mark_as_complete(args.task_id)
    elif args.action == 'remove':
        remove_task(args.task_id)
    elif args.action == 'show':
        show_tasks(args.sort_by_priority)

if __name__ == "__main__":
    main()
