
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


tasks = load_tasks()


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter your study task: ").strip()

    if not task:
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "done": False
    })

    save_tasks()
    print("Task added and saved successfully!")


def view_tasks():
    if not tasks:
        print("No study tasks added yet.")
        return

    print("\n===== YOUR STUDY TASKS =====")

    for number, item in enumerate(tasks, start=1):
        status = "Completed" if item["done"] else "Pending"
        print(f"{number}. {item['task']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks()
            print("Task completed and saved!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    total = len(tasks)
    completed = sum(1 for item in tasks if item["done"])
    pending = total - completed

    print("\n===== STUDY PROGRESS =====")
    print("Total tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)


while True:
    print("\n===== UPSC STUDY PLANNER V2 =====")
    print("1. Add study task")
    print("2. View study tasks")
    print("3. Complete a task")
    print("4. Show study progress")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        show_progress()
    elif choice == "5":
        print("Happy studying! Good luck for UPSC.")
        break
    else:
        print("Invalid choice. Try again.")
        
