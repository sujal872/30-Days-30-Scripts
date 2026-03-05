import os
FILE_NAME = "to-do-list.txt"

# Ensure file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass


# Add Task
def add_task():
    task = input("Enter Task: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{task}|{due_date}|Pending\n")

    print("✅ Task Added Successfully!\n")


# View Tasks
def view_tasks():
    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("📂 No tasks found.\n")
        return

    print("\n====== Your Tasks ======")
    for index, task in enumerate(tasks, start=1):
        task_name, due_date, status = task.strip().split("|")
        print(f"{index}. {task_name} | Due: {due_date} | Status: {status}")
    print()


# Delete Task
def delete_task():
    view_tasks()
    task_no = int(input("Enter Task Number to Delete: "))

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)

        with open(FILE_NAME, "w") as f:
            f.writelines(tasks)

        print("🗑️ Task Deleted Successfully!\n")
    else:
        print("❌ Invalid Task Number!\n")


# Mark Task as Completed
def mark_task():
    view_tasks()
    task_no = int(input("Enter Task Number to Mark as Completed: "))

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if 1 <= task_no <= len(tasks):
        task_name, due_date, status = tasks[task_no - 1].strip().split("|")
        tasks[task_no - 1] = f"{task_name}|{due_date}|Completed\n"

        with open(FILE_NAME, "w") as f:
            f.writelines(tasks)

        print("✔️ Task Marked as Completed!\n")
    else:
        print("❌ Invalid Task Number!\n")


def main():
    initialize_file()

    while True:
        print("====== To-Do List (File Based) ======")
        print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark Task as Completed\n5. Exit\n")
      
        try:
            choice = int(input("Choose Option: "))
        except ValueError:
            print("❌ Please enter a valid number!\n")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_task()
        elif choice == 5:
            print("👋 Exiting Program...")
            break
        else:
            print("❌ Invalid Choice!\n")


if __name__ == "__main__":
    main()