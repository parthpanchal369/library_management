class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_task(self):
        if not self.tasks:
            print("No task in todo_list")

        else:
            print("Todo List")
            for index, task in enumerate(self.tasks, start=1):
                status = "done" if task["completed"] else "pending"

                print(f"{index}.{task['task']} - {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed")

        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")
            todo_list.add_task(task)
            print("Task Added Successfully.")

        elif choice == "2":
            todo_list.view_task()

        elif choice == "3":
            try:
                task_index = int(input("Enter the task index to mark as completed: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            todo_list.mark_completed(task_index)

        elif choice == "4":
            print("Existing the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice!, Please enter the correct choice from 1 to 4. ")


if __name__ == "__main__":
    main()




