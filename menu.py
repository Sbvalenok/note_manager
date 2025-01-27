from colorama import init, Fore, Style, Back

from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes
from delete_note import delete_note
# Инициализация библиотеки
init(autoreset=True)

def display_menu(notes):
    while True:
        # Выводит на экран меню
        print(f"{Fore.LIGHTMAGENTA_EX}-" * 15)
        print(f"{Fore.BLACK}{Back.WHITE} Меню действий:")
        print(f"{Fore.LIGHTMAGENTA_EX}-" * 15)
        print(f"{Fore.CYAN}1. Создать новую заметку")
        print(f"{Fore.GREEN}2. Показать все заметки")
        print(f"{Fore.BLUE}3. Обновить заметку")
        print(f"{Fore.RED}4. Удалить заметку")
        print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}5. Найти заметки")
        print("6. Выйти из программы")

        # Блок проверки ввода и отображения ошибки ввода
        try:
            # Запрашиваем выбор пункта меню
            choice = input("\nВыберите пункт из меню: ")
            # Если 1, то вызывается функция создания новой заметки
            if choice == "1":
                note = create_note()
                notes.append(note)
            # Если 2, то вызывается функция отображения текущих заметок
            elif choice == "2":
                display_notes(notes)
            # Если 3, то функция обновления заметок
            elif choice == "3":
                if notes:
                    # Сначала показывает доступные заметки
                    display_notes(notes)
                    # Выбор заметки для изменения в соответствии с индексами списка заметок (нумерация с 0)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        # Если заметка существует, то вызывает функцию изменения заметки
                        notes[index] = update_note(notes[index])
                    else:
                        # Если заметки с таким номером нет, выводит сообщение об ошибке
                        print("Неверный номер заметки.")
                # Если список заметок пустой, то выводит сообщение на дисплей
                else:
                    print("Список заметок пуст.")
            # Если 4, то вызывается функция удаления заметки
            elif choice == "4":
                notes = delete_note(notes)
            # Если 5, то предлагает ввести ключевое слово для поиска и статус, далее вызывает функцию поиска заметок
            elif choice == "5":
                keyword = input("Введите ключевое слово для поиска: ")
                status = input("Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
                # Если 6, то заканчивает цикл и выводит на дисплей сообщении об окончании работы программы
            elif choice == "6":
                print("Программа завершена. Спасибо за использование!")
                break
            # Если введено другое число, сообщает об ошибке
            else:
                print("Неверный выбор. Попробуйте снова.")
        # Если введено не число
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")

# Запуск функции с использованием тестового списка заметок
if __name__ == "__main__":
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнена',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    display_menu(notes)