username = input('Введите Ваше имя: ')
content = input('Введите описание заметки: ')
status = input("Введите текущий статус заметки: ")
created_date = input("Введите дату сосздания заметки (В формате: дд-мм-гггг): ")
issue_date = input("Ввведите дату окончания (Дедлайн) заметки (В формате: дд-мм-гггг): ")
title1 = input('Введите 1-ый заголовок заметки: ')
title2 = input('Введите 2-ой заголовок заметки: ')
title3 = input('Введите 3-ий заголовок заметки: ')
title_list = [title1, title2, title3]
note = [
    username,
    content,
    status,
    created_date [0:5],
    issue_date [0:-5],
    title_list, # вложенный список для заголовков
]
print(note)
