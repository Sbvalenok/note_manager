# Сохранение заметок в файл

# Загружаем модуль для работы с датами
from datetime import datetime

# Создаем функцию сохранения заметок в файл
def save_notes_to_file(notes, filename):
    # Открываем файл для записи, после окончания работы он автоматически закроется
    with open(filename, 'w', encoding='UTF-8') as file:
        # Перебираем параметры заметки и указываем в каком виде необходимо вывести заметку на дисплей
        for note in notes:
            note_to_save = f"Имя пользователя: {note['username']}\n"
            note_to_save += f"Заголовок: {note['title']}\n"
            note_to_save += f"Описание: {note['content']}\n"
            note_to_save += f"Статус: {note['status']}\n"
            note_to_save += f"Дата создания: {note['current_date']}\n"
            note_to_save += f"Дедлайн: {note['issue_date']}\n"
            note_to_save += f"\n---\n"
            # Записываем полученные данные из заметки в текстовый файл
            file.write(note_to_save)

# Тестирование функции
if __name__ == '__main__':
    # Указываем текущую дату, в формате дд-мм-гггг
    current_date = str(datetime.now().strftime('%d-%m-%Y'))
    # Создаем тестовый список заметок
    notes = [
        {
            "username": "Имя_1",
            "title": "Заголовок_1",
            "content": "Описание_1",
            "status": "Статус_1",
            "current_date": current_date,
            "issue_date": "01-02-2025"
        },
        {
            "username": "Имя_2",
            "title": "Заголовок_2",
            "content": "Описание_2",
            "status": "Статус_2",
            "current_date": current_date,
            "issue_date": "01-03-2025"
        },
    ]
    # Вызываем функцию для записи в текстовый файл
    save_notes_to_file(notes, 'filename.txt')