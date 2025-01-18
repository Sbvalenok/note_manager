# Удаление заметок

# Создаем список заметок
notes = [
    {
        "id": "1",
        "username": "Павел",
        "title": "Ужин",
        "description": "Приготовить ужин"
    },
    {
        "id": "2",
        "username": "Антон",
        "title": "Пробежка",
        "description": "Выйти на пробежку"
    },
    {
        "id": "3",
        "username": "София",
        "title": "Праздник",
        "description": "Составить план мероприятия"
    }
]

# Выводим на экран список заметок
print("Список заметок:")
for note in notes:
    print(f"Заметка №{note["id"]}:")
    print(f"Имя: {note["username"]}")
    print(f"Заголовок: {note["title"]}")
    print(f"Описание: {note["description"]}\n")

# Запрашиваем у пользователя ввести позицию для удаления
delete_position = input("Введите имя пользователя или заголовок для удаления заметки: ")

# Проверяем что ввод не пустой
if not delete_position:
    print(" Ошибка ввода! Поле не может быть пустым. Пожалуйста введите имя пользователя или заголовок заметки.")

else:
    # Создаем два новых списка - заметки для удаления, и заметки которые оставляем
    notes_to_delete = []
    notes_to_save = []

    # Поиск заметок для удаления по имени пользователя или заголовку заметки
    for note in notes:
        if note["username"] == delete_position or note["title"] == delete_position:
            notes_to_delete.append(note)
        else:
            notes_to_save.append(note)

    # Если заметки для удаления не найдены, выводим на экран соответствующее сообщение
    if not notes_to_delete:
        print("Заметок с таким именем пользователя или заголовком не найдено")
    else:
        # Выводим на экран заметки которые будут удалены
        print("\nСледующие заметки будут удалены:")
        for note in notes_to_delete:
            print(f"Заметка №{note["id"]}:")
            print(f"Имя: {note["username"]}")
            print(f"Заголовок: {note["title"]}")
            print(f"Описание: {note["description"]}\n")

        # Запрашиваем подтверждение удаления указанных заметок
        confirm = input("Вы уверены что хотите удалить указанные заметки? Введите да или нет: ").strip().lower()

        if confirm == "да":
            # Обновляем список заметок в соответствии со списком заметок который хотим оставить
            notes = notes_to_save

            # Обновляем нумерацию заметок по порядку
            for i, note in enumerate(notes, 1):
                note["id"] = i

            # Выводим полученный результат
            print("\nВыбранные заметки удалены, список заметок обновлен.")
            if notes:
                print("\nОстались следующие заметки:\n")
                for note in notes:
                    print(f"Заметка №{note["id"]}:")
                    print(f"Имя: {note["username"]}")
                    print(f"Заголовок: {note["title"]}")
                    print(f"Описание: {note["description"]}\n")

            else:
                print("Список заметок пуст.")

        else:
            print("Удаление заметки отменено.")
