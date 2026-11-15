
tasks = []

def add_task():
    task = input("Enter your study task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No study tasks added yet.")
        return

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
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n===== UPSC STUDY PLANNER =====")
    print("1. Add study task")
    print("2. View study tasks")
    print("3. Complete a task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Happy studying! Good luck for UPSC.")
        break
    else:
        print("Invalid choice. Try again.")
      
