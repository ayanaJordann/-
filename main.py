#импортируем нужные нам библиотеки
import json
from PyQt6 import QtGui
from PyQt6.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QHBoxLayout, QTextEdit,QLabel, QListWidget,
                             QPushButton, QLineEdit, QInputDialog, QMessageBox)


#создаем обязательный объект класса QApplication
app = QApplication([])
# Создаем основное окно (виджет) приложения.
window = QWidget()
# Устанавливаем заголовок окна.
window.setWindowTitle('заметки')
# устанавливаем иконку для окна
window.setWindowIcon(QtGui.QIcon('note.png'))
# Устанавливаем минимальный размер окна.
window.setMinimumSize(600, 500)

# Создаём основной макет окна (горизонтальный)
main_layout = QHBoxLayout()
# Создаём вертикальный макет для левой части окна
col_left = QVBoxLayout()
# Создаём виджет для ввода и отображения текста заметки
text_note = QTextEdit()
# добавляем text_note в вертикальный макет col_left
col_left.addWidget(text_note)

# Создаём вертикальный макет для правой части окна
col_right = QVBoxLayout()

# Создаём вертикальный макет layout1
# для отображения списка заметок
layout1 = QVBoxLayout()

# Метка для списка заметок
lst_notes_label = QLabel('Список заметок:')
# Добавляем метку в layout1
layout1.addWidget(lst_notes_label)

# Виджет для отображения списка заметок
lst_notes = QListWidget()
# Добавляем список заметок в layout1
layout1.addWidget(lst_notes)

# Создаём горизонтальный макет layout2
# для кнопок создания и удаления заметок
layout2 = QHBoxLayout()

# Кнопка для создания заметки
btn_create_note = QPushButton('Создать заметку')
# Добавляем кнопку в layout2
layout2.addWidget(btn_create_note)

# Кнопка для удаления заметки
btn_delete_note = QPushButton('Удалить заметку')
# Добавляем кнопку в layout2
layout2.addWidget(btn_delete_note)

# Создаём вертикальный макет layout3
# для кнопок изменения и списка тегов
layout3 = QVBoxLayout()

# Кнопка для сохранения заметки
btn_save_note = QPushButton('Изменить заметку')
# Добавляем кнопку в layout3
layout3.addWidget(btn_save_note)

# Метка для списка тегов
tags_label = QLabel('Список тегов:')
# Добавляем метку в layout3
layout3.addWidget(tags_label)

# Виджет для отображения списка тегов
lst_tags = QListWidget()
# Добавляем список тегов в layout3
layout3.addWidget(lst_tags)

# Виджет для ввода тега
edit_tag = QLineEdit()
# Текст-подсказка в поле ввода
edit_tag.setPlaceholderText('Введите тег...')
# Добавляем поле ввода тега в layout3
layout3.addWidget(edit_tag)

# Создаём горизонтальный макет layout4
# для кнопок добавления и удаления тегов
layout4 = QHBoxLayout()

# Кнопка для добавления тега
btn_add_tag = QPushButton('Добавить к заметке')
# Добавляем кнопку в layout4
layout4.addWidget(btn_add_tag)

# Кнопка для удаления тега
btn_delete_tag = QPushButton('Открепить от заметки')
# Добавляем кнопку в layout4
layout4.addWidget(btn_delete_tag)

# Создаём горизонтальный макет layout5
# для кнопки поиска заметок по тегу
layout5 = QHBoxLayout()
# Кнопка для поиска по тегу
btn_search_by_tag = QPushButton('Искать заметки по тегу')
# Добавляем кнопку в layout5
layout5.addWidget(btn_search_by_tag)

# добавляем все макеты
col_right.addLayout(layout1)
col_right.addLayout(layout2)
col_right.addLayout(layout3)
col_right.addLayout(layout4)
col_right.addLayout(layout5)
# Устанавливаем расстояние между
# макетами в правой части окна
col_right.setSpacing(16)

# Добавляем левую и правую колонки в основной макет
main_layout.addLayout(col_left)
main_layout.addLayout(col_right)
# Устанавливаем основной макет для окна
window.setLayout(main_layout)

# Загрузка данных из файла notes.json (если существует),
# иначе создаём пустой словарь
try:
    with open('notes.json', 'r', encoding='utf-8') as file:
        # Загружаем данные из файла JSON
        data = json.load(file)
except FileNotFoundError:
    data = {}
    # Если файл не найден,
    # создаём пустой словарь для данных

  # Заполняем список заметок именами из загруженных данных
lst_notes.addItems(data.keys())


# функция для показа текста и тегов заметки
def show_note():
    # Получаем название выбранной заметки
    note_name = lst_notes.currentItem().text()
    # Получаем текст заметки из данных
    n_text = data[note_name]["text"]
    # Получаем теги заметки из данных
    n_tags = data[note_name]["tags"]

    # Отображаем текст заметки в текстовом поле
    text_note.setText(n_text)
    # Очищаем список тегов
    lst_tags.clear()
    # Заполняем список тегов тегами из данных
    lst_tags.addItems(n_tags)


# Привязываем сигнал нажатия на элемент
# списка заметок к функции show_note
lst_notes.itemClicked.connect(show_note)


# функция для создания новой заметки
def create_note():
    # Открываем диалоговое окно для ввода названия заметки
    note_name, result = QInputDialog.getText(window, \
                                             "Добавить заметку", "Название заметки:")
    if result and not note_name in data.keys() and note_name != '':
        # Проверяем, что ввели имя, его нет в словаре и оно не пустое
        data[note_name] = {
            "text": "",
            "tags": []
        }
        # Создаём новую запись в словаре с пустым текстом и списком тегов
        # Добавляем имя заметки в список
        lst_notes.addItem(note_name)


# Привязываем сигнал нажатия на кнопку
# создания заметки к функции create_note
btn_create_note.clicked.connect(create_note)


# функция для сохранения всех данных в файл notes.json
def save_all():
    # Сохраняем данные в JSON с отступами и поддержкой кириллицы
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# функция для сохранения изменений в текущей заметке
def save_note():
    # Проверяем, выбрана ли заметка в списке
    if lst_notes.currentItem():
        # Получаем название выбранной заметки
        note_name = lst_notes.currentItem().text()
        # Обновляем текст заметки
        data[note_name]['text'] = text_note.toPlainText()
        # Сохраняем все данные
        save_all()


# Привязываем сигнал нажатия на кнопку
# сохранения заметки к функции save_note
btn_save_note.clicked.connect(save_note)


# функция для удаления заметки
def delete_note():
    # Проверяем, выбрана ли заметка в списке
    if lst_notes.currentItem():
        # Получаем название выбранной заметки
        note_name = lst_notes.currentItem().text()
        # Удаляем заметку из словаря
        del data[note_name]

        # Получаем индекс выбранной заметки
        cur_row = lst_notes.currentRow()
        # Удаляем заметку из списка
        lst_notes.takeItem(cur_row)

        # Очищаем список тегов
        lst_tags.clear()
        # Очищаем текстовое поле
        text_note.clear()


# Привязываем сигнал нажатия на кнопку
# удаления заметки к функции delete_note
btn_delete_note.clicked.connect(delete_note)


# функция для добавления тега к заметке
def add_tag():
    # Открываем диалоговое окно для ввода названия тега
    tag_name, result = QInputDialog.getText(window, \
                                            "Добавить тег к заметке", "Название тега:")
    # Проверяем, выбрана ли заметка и введён ли тег
    if lst_notes.currentItem() and result and len(tag_name) > 0:
        # Получаем название выбранной заметки
        note_name = lst_notes.currentItem().text()
        # Добавляем тег в список тегов заметки
        data[note_name]['tags'].append(tag_name)
        # Добавляем тег в список тегов в интерфейсе
        lst_tags.addItem(tag_name)
        # Сохраняем все данные
        save_all()


# Привязываем сигнал нажатия на кнопку
# добавления тега к функции add_tag
btn_add_tag.clicked.connect(add_tag)


# функция для удаления тега из заметки
def delete_tag():
    # Проверяем, выбраны ли заметка и тег
    if lst_notes.currentItem() and lst_tags.currentItem():
        # Получаем название выбранной заметки
        note_name = lst_notes.currentItem().text()
        # Получаем название выбранного тега
        tag_name = lst_tags.currentItem().text()
        # Удаляем тег из списка тегов заметки
        data[note_name]['tags'].remove(tag_name)

        # Получаем индекс выбранного тега
        cur_row = lst_tags.currentRow()
        # Удаляем тег из списка в интерфейсе
        lst_tags.takeItem(cur_row)
        # Сохраняем все данные
        save_all()


# Привязываем сигнал нажатия на кнопку
# удаления тега к функции delete_tag
btn_delete_tag.clicked.connect(delete_tag)


# функция для поиска заметок по тегу
def find_by_tag():
    # Проверяем, нужно ли искать или сбросить
    if btn_search_by_tag.text() != 'Сбросить результаты поиска':
        # Проверяем, что в поле поиска введен тег
        if len(edit_tag.text()) > 0:
            # Получаем тег из поля ввода
            text_to_find = edit_tag.text()
            # Создаём словарь для хранения результатов поиска
            result = {}
            # Итерируем по всем заметкам
            for key, value in data.items():
                # Проверяем, есть ли искомый тег в заметке
                if text_to_find in value['tags']:
                    # Если есть - добавляем заметку в результаты
                    result[key] = value

            # Очищаем список заметок
            lst_notes.clear()
            # Очищаем список тегов
            lst_tags.clear()
            # Очищаем текстовое поле
            text_note.clear()
            # Добавляем отфильтрованные заметки в список
            lst_notes.addItems(result.keys())

            # меняем текст кнопки на сброс
            btn_search_by_tag.setText('Сбросить результаты поиска')
        else:
            # Выводим предупреждение, если тег не введен
            msg = QMessageBox.warning(window, 'Предупреждение', 'Вы не ввели тег для поиска')
    # Если режим сброса
    else:
        # Очищаем список заметок
        lst_notes.clear()
        # Очищаем список тегов
        lst_tags.clear()
        # Очищаем текстовое поле
        text_note.clear()
        # Загружаем все заметки
        lst_notes.addItems(data.keys())
        # меняем текст кнопки на поиск
        btn_search_by_tag.setText('Искать заметки по тегу')

# Привязываем сигнал нажатия на кнопку
# поиска заметок по тегу к функции find_by_tag
btn_search_by_tag.clicked.connect(find_by_tag)

# Отображаем главное окно
window.show()
# Запускаем основной цикл приложения
app.exec()
