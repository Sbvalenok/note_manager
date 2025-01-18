# Обработка дедлайнов

# Импортируем модуль для работы с датой
from datetime import datetime 

# Выводим на экран текущую дату без отображения времени
current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

print(f"Сегодня: {current_date.strftime('%d/%m/%Y')}")

# Основной блок программы
while True: # Запускаем цикл ввода даты пользователем и проверки Дедлайна
    try:
        # Запрашиваем дату Дедлайна у пользователя
        deadline_now = input("Введите дату Дедлайна (в формате ДД/ММ/ГГГГ, например 15/01/2025): ")

        # Преобразуем строку с датой в объект datetime
        deadline_date = datetime.strptime(deadline_now, "%d/%m/%Y").replace(hour=0, minute=0, second=0, microsecond=0)

        # Вычисляем разницу между текущей датой и Дедлайном в днях
        time_difference = deadline_date - current_date
        days_difference = time_difference.days

        # Проверяем статус Дедлайна и выводим соответствующее сообщение
        if days_difference < 0:
            print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До Дедлайна осталось {days_difference:02d} дней.")

        # Прерываем цикл после успешной обработки даты
        break

    # Обработка ошибки неверного формата даты
    except ValueError:
        print("Ошибка! Пожалуйста, введите дату в правильном формате (ДД/ММ/ГГГГ).")
        print("Пример: 15/01/2025")
