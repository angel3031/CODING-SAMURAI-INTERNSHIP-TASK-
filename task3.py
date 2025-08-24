todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        print("Task added!")
    else:
        print("Task cannot be empty.")

def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
