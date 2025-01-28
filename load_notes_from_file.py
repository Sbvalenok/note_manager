# Загрузка заметок из файла

# Создаем функцию для чтения заметки из файла .txt
def load_notes_from_file(filename):
    notes = []
    translate_table = {
        "Имя пользователя": "username",
        "Заголовок": "title",
        "Описание": "content",
        "Статус": "status",
        "Дата создания": "created_date",
        "Дедлайн": "issue_date"
    }
    with open(filename, 'r', encoding='UTF-8') as file:
        content = file.read()
        if content:
            note_blocks = content.split("\n---\n")
            for block in note_blocks:
                note_lines = block.split("\n")
                note = {}
                for line in note_lines:
                    verbose_key, value = line.split(": ", 1)
                    key = translate_table[verbose_key]
                    note[key] = value
                notes.append(note)
    return notes

if __name__ == '__main__':
    notes = load_notes_from_file("filename.txt")
    for note in notes:
        print(note)