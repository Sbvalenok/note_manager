username = input('Введите Ваше имя: ')
title1 = input('Введите 1-ый заголовок заметки: ')
title2 = input('Введите 2-ой заголовок заметки: ')
title3 = input('Введите 3-ий заголовок заметки: ')
title_list = [title1, title2, title3]
content = input('Введите описание заметки: ')
status = input("Введите текущий статус заметки: ")
created_date = input("Введите дату сосздания заметки (В формате: дд-мм-гггг): ")
issue_date = input("Ввведите дату окончания (Дедлайн) заметки (В формате: дд-мм-гггг): ")

print('Имя пользователя: ', username)
print('Первый заголовок заметки:', title_list[0])
print('Второй заголовок заметки:', title_list[1])
print('Третий заголовок заметки:', title_list[2])
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', created_date[0:5])
print('Дата окончания заметки (Дедлайн):', issue_date[:-5])