def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_completed(tasks, index):
    if index >= len(tasks) or index < 0:
        print("Invalid task index.")
    else:
        tasks[index] += " (Completed)"
        print("Task marked as completed!")

def delete_task(tasks, index):
    if index >= len(tasks) or index < 0:
        print("Invalid task index.")
    else:
        del tasks[index]
        print("Task deleted successfully!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter the index of the task to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
