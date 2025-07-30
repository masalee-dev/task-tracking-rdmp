import json
import os

TASK_FILE = 'task-tracker.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return {"last_id":0, "tasks": []}

def save_tasks(data):
    with open(TASK_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_task(description):
    data = load_tasks()
    data["last_id"] += 1
    task_id = data["last_id"]
    data['tasks'].append({'id': task_id, 'description': description, 'done':False})
    save_tasks(data)
    print(f"Task success added (ID: {task_id})")

def list_tasks():
    data = load_tasks()
    if not data['tasks']:
        print('No Tasks yet.')
        return
    for task in data['tasks']:
        status = '👍' if task['done'] else '👎'
        print(f"[{status}] {task['id']}: {task['description']}")

def mark_done(task_id):
    data = load_tasks()
    for task in data['tasks']:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(data)
            print(f"Task {task_id} marked as done!")
            return
    print(f"No task found with ID {task_id}.")

def delete_task(task_id):
    data = load_tasks()
    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)
            save_tasks(data)
            print(f"Task {task_id} deleted.")
            return
    print(f"No task found with ID {task_id}.")

# example CLI usage

if __name__ == '__main__':
    while True:
        print('\n----- Task Tracker Using CLI -----')
        print('1. Add task')
        print('2. List task')
        print('3. Mark task as done')
        print('4. Delete task')
        print('5. Exit')
        choice = input("Choose an option: ")

        if choice == '1':
            desc = input('Task Description: ')
            add_task(desc)
        elif choice =='2':
            list_tasks()
        elif choice == '3':
            task_id = int(input('Enter task ID to mark as done: '))
            mark_done(task_id)
        elif choice =='4':
            task_id = int(input('Enter task ID to delete: '))
        elif choice == '5':
            break
        else:
            print('Invalid Option!')