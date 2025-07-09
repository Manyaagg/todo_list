# todo_list_in_memory.py

todo_list = []
task_id = 0

def add_task(task):
    global task_id
    task_id += 1
    todo_list.append({"id": task_id, "task": task, "completed": False})
    print(f"Task '{task}' added with ID {task_id}.")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return

    print("\n--- Your To-Do List ---")
    for item in todo_list:
        status = "✓" if item["completed"] else " "
        print(f"[{status}] ID: {item['id']} - {item['task']}")
    print("-----------------------\n")

def mark_task_complete(task_id_to_complete):
    found = False
    for item in todo_list:
        if item["id"] == task_id_to_complete:
            item["completed"] = True
            print(f"Task ID {task_id_to_complete} marked as complete.")
            found = True
            break
    if not found:
        print(f"Task with ID {task_id_to_complete} not found.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id_input = int(input("Enter the ID of the task to mark complete: "))
                mark_task_complete(task_id_input)
            except ValueError:
                print("Invalid input. Please enter a number for the task ID.")
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()