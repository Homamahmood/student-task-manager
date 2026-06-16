tasks = []


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split("|")

                task = {
                    "name": task_data[0],
                    "done": task_data[1] == "True",
                    "priority": task_data[2]
                }

                tasks.append(task)

    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
                f"{task['name']}|{task['done']}|{task['priority']}\n"
            )


def show_menu():
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")

    else:
        print("\nYour Tasks:")

        for index, task in enumerate(tasks, start=1):

            status = "✅" if task["done"] else "❌"

            print(
                f"{index}. [{status}] "
                f"[{task['priority']}] "
                f"{task['name']}"
            )


load_tasks()


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        task_name = input("Enter task: ")

        priority = input(
            "Enter priority (High/Medium/Low): "
        ).capitalize()

        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"

        task = {
            "name": task_name,
            "done": False,
            "priority": priority
        }

        tasks.append(task)

        save_tasks()

        print("Task added successfully!")

    elif choice == "2":
        view_tasks()

    elif choice == "3":

        view_tasks()

        if len(tasks) > 0:

            try:
                task_number = int(
                    input("Enter task number to complete: ")
                )

                if 1 <= task_number <= len(tasks):

                    tasks[task_number - 1]["done"] = True

                    save_tasks()

                    print("Task marked as completed!")

                else:
                    print("Invalid task number")

            except ValueError:
                print("Please enter a valid number")

    elif choice == "4":

        view_tasks()

        if len(tasks) > 0:

            try:
                task_number = int(
                    input("Enter task number to delete: ")
                )

                if 1 <= task_number <= len(tasks):

                    removed_task = tasks.pop(task_number - 1)

                    save_tasks()

                    print(
                        f"Deleted: {removed_task['name']}"
                    )

                else:
                    print("Invalid task number")

            except ValueError:
                print("Please enter a valid number")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")