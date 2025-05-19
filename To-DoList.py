def add_tasks():
    print("Let's add 3 tasks to your to-do list.")
    tasks = []
    tasks.append(input("Enter task 1: "))
    tasks.append(input("Enter task 2: "))
    tasks.append(input("Enter task 3: "))
    return tasks

def show_tasks(tasks):
    print("\nHere are your tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

todo_list = add_tasks()
show_tasks(todo_list)
