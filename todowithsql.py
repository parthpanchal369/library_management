import sqlite3


class TodoList:
    def __init__(self):
        self.conn = sqlite3.connect('todo_list.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        self.conn.commit()

    def view_task(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()

        if not tasks:
            print("No tasks in the To-Do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task[2] else "Pending"
                print(f"{index}. {task[1]} - {status}")

    def mark_completed(self, task_index):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()

        if 1 <= task_index <= len(tasks):
            task_id = tasks[task_index - 1][0]
            cursor.execute('UPDATE tasks SET completed=1 WHERE id=?', (task_id,))
            self.conn.commit()
            print("Task marked as completed.")
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
            print("Exiting the To-Do List application. Goodbye!")
            todo_list.conn.close()
            break

        else:
            print("Invalid choice! Please enter the correct choice from 1 to 4.")


if __name__ == "__main__":
    main()


def print_database(self):
    cursor = self.conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    print("Data in the database:")
    for task in tasks:
        print(task)

