tasks = []
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!\n")
    elif choice == "2":
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()
    elif choice == "3":
        print("Exiting the To-Do List")
        break
    else:
        print("Invalid choice.\n")
        2
