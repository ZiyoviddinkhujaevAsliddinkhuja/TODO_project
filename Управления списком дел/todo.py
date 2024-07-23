FILENAME = "tasks.txt"

def show_menu():
    print("\nМеню:")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить задачу как выполненную")
    print("5. Выйти")

def show_tasks(tasks):
    if not tasks:
        print("Задач нет.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(f"[ ] {task}")
    print(f"Задача '{task}' добавлена.")
    save_tasks(tasks)

def delete_task(tasks):
    show_tasks(tasks)
    task_number = int(input("Введите номер задачи для удаления: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Задача '{removed_task}' удалена.")
        save_tasks(tasks)
    else:
        print("Неверный номер задачи.")

def mark_task_as_done(tasks):
    show_tasks(tasks)
    task_number = int(input("Введите номер задачи для отметки как выполненной: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[✓]", 1)
        print(f"Задача '{tasks[task_number - 1]}' отмечена как выполненная.")
        save_tasks(tasks)
    else:
        print("Неверный номер задачи.")

def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    except Exception as e:
        print(f"Ошибка при загрузке задач: {e}")
        tasks = []
    return tasks

def save_tasks(tasks):
    try:
        with open(FILENAME, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_as_done(tasks)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()



