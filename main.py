import json
import os
from datetime import datetime


# Создание заметки
def add_note(notes, title_note, body_note):
    new_note = {
        "id": len(notes) + 1,
        "title": title_note,
        "body": body_note,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(new_note)
    save_note(notes)
    print("Заметка успешно создана")


# Сохранение заметок в файл
def save_note(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)


# Чтение данных из файла
def load_note():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []


# Вывод списка заметок с выборкой по дате
def note_by_date(notes, filter_date=None):
    for note in notes:
        if filter_date:
            note_date = datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S")
            if note_date.date() != filter_date:
                continue

        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print("\n")


# Редактирование заметки
def edit_note(notes, id_note, new_title_note, new_body_note):
    for note in notes:
        if note["id"] == id_note:
            note["title"] = new_title_note
            note["body"] = new_body_note
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_note(notes)
            print("Заметка успешно отредактирована")
            return
    print("Введен некорректный индекс заметки")


# Удаление заметки
def delete_note(notes, id_note):
    for note in notes:
        if note["id"] == id_note:
            notes.remove(note)
            save_note(notes)
            print('Заметка успешно удалена')
            return
    print("Введен некорректный индекс заметки")


# Вывод всего списка заметок
def output_list_note(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print("\n")


# Вывод одной заметки
def output_note(notes, id_note):
    for note in notes:
        if note["id"] == id_note:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки: {note['body']}")
            print(f"Дата/время создания: {note['timestamp']}")
            break
        else:
            print("Заметка не найдена")
            break


# Основная функция
def main():
    notes = load_note()

    while True:
        print("""  
        1. add - добавить заметку
        2. edit - редактировать заметку
        3. delete - удалить заметку
        4. date - вывести список заметок по дате
        5. list - вывести весь список заметок
        6. note - вывести одну заметку
        """)
        command = int(input("Введите команду: "))

        if command == 1:
            title_note = input("Введите заголовок заметки: ")
            body_note = input("Введите тело заметки: ")
            add_note(notes, title_note, body_note)
        elif command == 2:
            id_note = int(input("Введите индекс заметки: "))
            new_title_note = input("Введите новый заголовок заметки: ")
            new_body_note = input("Введите новое тело заметки: ")
            edit_note(notes, id_note, new_title_note, new_body_note)
        elif command == 3:
            id_note = int(input("Введите индекс заметки: "))
            delete_note(notes, id_note)
        elif command == 4:
            new_date = input("Введите дату в формате YYYY-MM-DD: ")
            filter_date = datetime.strptime(new_date, "%Y-%m-%d").date()
            note_by_date(notes, filter_date)
        elif command == 5:
            output_list_note(notes)
        elif command == 6:
            id_note = int(input("Введите индекс заметки: "))
            output_note(notes, id_note)
        else:
            print("Введена некорректная команда")


if __name__ == "__main__":
    main()
