#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLabel, QVBoxLayout, QHBoxLayout,QListWidget, QTextEdit, QLineEdit

#приложение
app = QApplication([])
notes = []
winda = QWidget()
winda.setWindowTitle("Заметки samvung GW 2021+")
winda.resize(900, 600)

#настройка
list_notes = QListWidget()
list_not_text = QLabel("Список заметок :)")
list_tag = QListWidget()
list_tag_text = QLabel("Список тегов :)")

button_create = QPushButton("Создать заметку ;)")
button_del = QPushButton("Удалить :(")
button_save = QPushButton("сохранить :)")
button_tag_add = QPushButton("Добавить к заметке")
button_tag_del = QPushButton("открепить")
button_tag_search = QPushButton("Искать заметку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введи тег")
field_text = QTextEdit()

ln = QHBoxLayout()
l1 = QVBoxLayout()
l2 = QVBoxLayout()

l1.addWidget(field_text)

l2.addWidget(list_not_text)
l2.addWidget(list_notes)

l_row1 = QHBoxLayout()
l_row1.addWidget(button_del)
l_row1.addWidget(button_create)

l_row2 = QHBoxLayout()
l_row2.addWidget(button_save)

l2.addLayout(l_row1)
l2.addLayout(l_row2)

l2.addWidget(list_tag_text)
l2.addWidget(list_tag)
l2.addWidget(field_tag)

l_row3 = QHBoxLayout()
l_row3.addWidget(button_tag_add)
l_row3.addWidget(button_tag_del)

l_row4 = QHBoxLayout()
l_row4.addWidget(button_tag_search)

l2.addLayout(l_row3)
l2.addLayout(l_row4)

ln.addLayout(l1)
ln.addLayout(l2)

winda.setLayout(ln)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tag.clear()
            list_tag.addItems(note[2])
    
    

def add_note():
    note_name, ok = QInputDialog.getText(winda, "ДОБАВЬ ЗАМЕТКУ", "название заметки")
    if ok and note_name != "":
        note = list()
        note = [note_name, "", ""]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tag.addItems(notes[2])
        print(notes)
        with open(str(len(notes)-1) + ".txt", "w") as file:
            file.write(note[0] + "\n")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index) + ".txt", "w") as file:
                    file.write(note[0] + "\n")
                    file.write(note[1] + "\n")
                    for tag in note[2]:
                        file.write(tag + " ")
                    file.write("\n")
            index += 1
        print(notes)
    else:
        print("А ГДЕ ЗАМЕТКААА!!!!")

def del_note():
    pass

def add_tag():
    pass

def del_tag():
    pass

def search_tag():
    pass


list_notes.itemClicked.connect(show_note)

button_create.clicked.connect(add_note)
button_save.clicked.connect(save_note)
button_del.clicked.connect(del_note)

button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)

winda.show()
name = 0
note = []
while True:
    filename = str(name) + ".txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "")
                note.append(line)
        tags = note[2].split()
        note[2] = tags
        notes.append(note)
        note = []
        name += 1
    except IOError:
        break
print(notes)
for note in notes:
    list_notes.addItem(note[0])
app.exec_()