tasks = []

while True:
    print("""
TODO Manager
1. Add task
2. Show tasks
3. Delete task
4. Exit
""")
    choice = int(input("> "))
    
    if choice == 1:
        x = input("New task: ")
        tasks.append(x)
        print("Task added!")
        
    elif choice == 2:
        if not tasks:
            print("No tasks yet!")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
                
    elif choice == 3:
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid task number!")
                
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
