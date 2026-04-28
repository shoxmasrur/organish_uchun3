from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

app = QApplication([])
win = QWidget()

win.setWindowTitle("First App")
win.setFixedSize(500, 250)

edit_name = QLineEdit(win)
edit_name.move(50, 10)
edit_name.setStyleSheet("font-size: 20px")
edit_name.setPlaceholderText("name:")

edit_email= QLineEdit(win)
edit_email.move(200, 10)
edit_email.setStyleSheet("font-size: 20px")
edit_email.setPlaceholderText("email:")

edit_age = QLineEdit(win)
edit_age.move(403, 10)
edit_age.setStyleSheet("font-size: 20px")
edit_age.setPlaceholderText("age:")

def yangi():
    edit_name.clear()
    edit_email.clear()

def age():
    yosh=int(edit_age.text())

btn_clear = QPushButton("clear", win)
btn_clear.move(200, 50)
btn_clear.clicked.connect(yangi)


btn_ok = QPushButton("OK", win)
btn_ok.move(150, 100)
btn_ok.clicked.connect(age)





win.show()
app.exec_()
