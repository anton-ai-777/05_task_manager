tasks = ["Изучить Python", "Создать AI-бота", "Загрузить проект на GitHub"]

print("===== Task Manager =====")
print()

print("1. Показать задачи")
print("2. Добавить задачу")
print("3. Удалить задачу")
print("4. Отметить задачу выполненной")
print("5. Выход")
print()

choice = input("Выберите действие: ")

if choice == "1":
    print()
    print("Список задач:")
    print()

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

elif choice == "2":
    new_task = input("Введите новую задачу: ")

    tasks.append(new_task)

    print()
    print("Задача успешно добавлена!")
    print()

    print("Список задач:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

elif choice == "3":
    print()
    print("Список задач:")
    print()

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()

    number = int(input("Введите номер задачи для удаления: "))

    tasks.pop(number - 1)

    print()
    print("✅ Задача успешно удалена!")
    print()

    print("Список задач:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

elif choice == "4":
    print()
    print("Список задач:")
    print()

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()

    number = int(input("Введите номер выполненной задачи: "))

    tasks[number - 1] = "✅ " + tasks[number - 1]

    print()
    print("Задача отмечена как выполненная!")
    print()

    print("Список задач:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

elif choice == "5":
    print("До свидания!")

else:
    print("Неверный выбор")
