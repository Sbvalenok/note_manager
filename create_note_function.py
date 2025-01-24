# Функция создания заметки

# Загружаем модуль из библиотеки для работы с датой
from datetime import datetime

# Создаем функцию для ввода заметки
def create_note():
    # Выводим на экран заголовок действия
    print(' "Создание новой заметки" ')

    # Блок ввода имени пользователя
    username = input("Введите имя пользователя: ").strip().capitalize()
    # Цикл проверки пустого ввода
    while not username:
        print("Имя пользователя не может быть пустым")
        username = input("Введите имя пользователя: ").strip().capitalize()

    # Блок ввода заголовка заметки
    title = input("Введите заголовок заметки: ").strip().capitalize()
    # Цикл проверки пустого ввода
    while not title:
        print("Заголовок заметки не может быть пустым")
        title = input("Введите заголовок заметки: ").strip().capitalize()

    # Блок ввода описания заметки
    content = input("ВВедите описание заметки: ").strip().capitalize()
    # Цикл проверки пустого ввода
    while not content:
        print("Описание заметки не может быть пустым")
        content = input("ВВедите описание заметки: ").strip().capitalize()

    # Блок ввода статуса заметки

    # Создаем список возможных статусов
    status_options = ["новая", "в процессе", "выполнена"]
    # Запрашиваем ввод статуса и показываем возможные варианты статусов из списка
    status = input(f"Введите статус заметки ({"/".join(status_options)}): ").strip().lower()
    while status not in status_options:
        print(f"Вы ввели неверный статус. Возможные варианты: {", ".join(status_options)}")
        status = input(f"Введите статус заметки ({"/".join(status_options)}): ").strip().lower()

    # Присваиваем дате создание заметки текущую дату используя модуль datetime
    create_date = datetime.now().strftime("%d:%m:%Y")

    # Блок ввода даты Дедлайна
    # Запускаем цикл ввода Дедлайна
    while True:
        # Запрашиваем ввод даты Дедлайна и проверяем соответствие формата ввода
        try:
            issue_date = input(f"Введите дату Дедлайна (в формате - дд:мм:гггг): ").strip()
            datetime.strptime(issue_date, "%d:%m:%Y")
            break
        # Если формат неверный, выводим сообщение об ошибке и просим ввести дату Дедлайна снова
        except ValueError:
            print("Неверный формат даты.")

    # Создаем словарь с данными заметки
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "create_date": create_date,
        "issue_date": issue_date
    }

    # Возвращаем созданный словарь из функции
    return note

# Выводим полученный результат
if __name__ == "__main__":
    note = create_note()
    print("\nЗаметка создана:", note)
