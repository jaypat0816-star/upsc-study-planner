
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


def add_task():
    print("\n--- ADD STUDY TASK ---")

    subject = input("Enter subject (Polity/History/Geography/Economy): ")
    task = input("Enter study task: ")
    deadline = input("Enter deadline (YYYY-MM-DD) or press Enter to skip: ")

    if not subject.strip() or not task.strip():
        print("Subject and task cannot be empty.")
        return

    if deadline:
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    new_task = {
        "subject": subject,
        "task": task,
        "deadline": deadline or "Not set",
        "done": False
    }

    tasks.append(new_task)
    save_tasks()

    print("\nTask added successfully!")


def view_tasks():
    print("\n--- YOUR STUDY TASKS ---")

    if not tasks:
        print("No tasks available.")
        return

    for number, item in enumerate(tasks, start=1):
        status = "Completed" if item["done"] else "Pending"

        print(f"\n{number}. {item['task']}")
        print(f"   Subject: {item['subject']}")
        print(f"   Deadline: {item['deadline']}")
        print(f"   Status: {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    total = len(tasks)
    completed = sum(1 for item in tasks if item["done"])

    print("\n--- STUDY PROGRESS ---")
    print("Total tasks:", total)
    print("Completed:", completed)
    print("Pending:", total - completed)

    if total > 0:
        percentage = (completed / total) * 100
        print(f"Progress: {percentage:.1f}%")


def main():
    while True:
        print("\n===== UPSC STUDY PLANNER =====")
        print("1. Add study task")
        print("2. View study tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Show study progress")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_progress()
        elif choice == "6":
            print("Good luck with your UPSC preparation!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
