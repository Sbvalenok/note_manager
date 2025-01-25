# Функция отображения заметок

# Функция создания страниц, на одной странице 5 заметок (notes[0:5] - первая страница, notes[5:10] - вторая страница)
def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5

    # Функция нумерации заметок в списке, формат вывода заметки на дисплей
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки f string
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание: {note["content"]}
        Статус: {note["status"]}
        Дата создания: {note["create_date"]}
        Дедлайн: {note["issue_date"]}
        """)
        # Визуальный разделитель заметок
        print("=" * 40)  # str * int

# Функция отображения заметок
def display_notes(notes, page_number=0):
    # Проверка на пустой список заметок
    if len(notes) == 0:
        print("Список заметок пуст")
    # Если в списке есть заметки, выводит на дисплей указанную страницу с заметками (по 5 заметок на одной странице)
    else:
        display_page(notes, page_number)

# Создаем тестовый список заметок
if __name__ == '__main__':
    notes = [
        {"username": "1", "title": "Заголовок 1", "content": "Описание 1", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025" },
        {"username": "2", "title": "Заголовок 2", "content": "Описание 2", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "3", "title": "Заголовок 3", "content": "Описание 3", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "4", "title": "Заголовок 4", "content": "Описание 4", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "5", "title": "Заголовок 5", "content": "Описание 5", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "6", "title": "Заголовок 6", "content": "Описание 6", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "7", "title": "Заголовок 7", "content": "Описание 7", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "8", "title": "Заголовок 8", "content": "Описание 8", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "9", "title": "Заголовок 9", "content": "Описание 9", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
        {"username": "10", "title": "Заголовок 10", "content": "Описание 10", "status": "новая",
         "create_date": "25-01-2025", "issue_date": "30-01-2025"},
    ]
    # Выводим на экран первую страницу списка
    display_notes(notes=notes, page_number=0)

    # Выводим на экран вторую страницу списка
    display_notes(notes=notes, page_number=1)