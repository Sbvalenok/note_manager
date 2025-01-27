# Функция для поиска заметок

# Создаем функцию для поиска заметок
def search_notes(notes, keyword=None, status=None):
    # Создаем список ключей из словаря заметки в которых будем искать введенные данные для keyword
    fields_for_search = ["username", "content", "title"]
    # Создаем пустой список в который будем помещать найденные заметки
    found_notes = []

    # Запускаем цикл проверки введенного значения в существующих заметках
    for note in notes:
        keyword_criteria = True
        status_criteria = True

        if keyword is not None:
            for field in fields_for_search:
                if note[field] == keyword:
                    keyword_criteria = True
                else:
                    keyword_criteria = False
        if status is not None:
            if note["status"] == status:
                status_criteria = True
            else:
                status_criteria = False
        # Если значения обнаружены в существующих заметках, то перемещаем их в список найденных заметок
        if keyword_criteria == True and status_criteria == True:
            found_notes.append(note)

    # Возвращаем список найденных заметок
    return found_notes

if __name__ == '__main__':
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнена',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    print("-" * 15)
    print(" Поиск заметок")
    print("-" * 15)
    print('''
Для выбора критерия поиска необходимо ввести число (1, 2, 3):
1 - поиск по ключевому слову; 
2 - поиск по статусу; 
3 - поиск по обоим критериям (ключевое слово и статус).
Для выхода из поиска оставьте поле пустым.
''')
    # Запускаем цикл ввода данных от пользователя
    while True:
        value_for_search = input("Введите число от 1 до 3, либо оставьте поле пустым для выхода: ").strip()
        # Проверяем что бы пользователь ввел десятичное число
        if value_for_search.isdecimal():
            value_for_search = int(value_for_search)
        # Если поле оставлено пустым, то завершаем цикл ввода и выводим на дисплей сообщение о завершении
        if not value_for_search:
            print("Поиск заметок завершен")
            break

        elif value_for_search == 1:
            # Запрашиваем ввод ключевого слова для поиска
            word_search = input('Введите ключевое слово: ').strip()
            # Поиск введенных данных в ключах словарей заметок
            found_notes = search_notes(notes, keyword=word_search)

        elif value_for_search == 2:
            # Запрашиваем ввод статуса для поиска с возможными вариантами статуса
            status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Создаем список возможных статусов
            variable_status = ["новая", "в процессе", "выполнена"]
            # Обработка ошибочного ввода
            while status_search not in variable_status:
                print(f"Ошибка ввода! Статус {status_search} не найден.")
                status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Поиск введенного статуса в статусах существующих заметок
            found_notes = search_notes(notes, status=status_search)

        elif value_for_search == 3:
            # Запрашиваем ввод обоих критериев
            word_search = input('Введите ключевое слово: ').strip()
            status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Поиск в существующих заметках по обоим критериям
            found_notes = search_notes(notes, keyword=word_search, status=status_search)

        # Обработка ввода других значений
        else:
            # Сообщение об ошибке с возможными вариантами ввода
            print('''
Ошибка ввода, необходимо ввести число от 1 до 3.
Повторите ввод, либо оставьте поле пустым что бы завершить поиск заметок
''')
            # Возвращаемся в начало цикла
            continue
        # Если заметки не найдены и список поиска заметок пустой, то выводим сообщение на дисплей
        if found_notes == []:
            print("-" * 20)
            print(" Заметка не найдена")
            print("-" * 20)
        # Если заметки найдены, выводим их на экран в комфортном для восприятия формате
        else:
            print("\n" + "-" * 45)
            print(" По вашему запросу найдены следующие заметки")
            print("-" * 45)
            for i in found_notes:
                print(f"""
Имя пользователя: {i['username']}
Заголовок: {i['title']}
Содержание: {i['content']}
Статус: {i['status']}
Дата создания: {i['created_date']}
Дедлайн: {i['issue_date']}
""")
                print("=" * 80)
