import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks  2. Add Task  3. Mark Done  4. Delete Task  5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
