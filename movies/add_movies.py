import json
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Yangi film qo'shish ilovasi")
        self.setFixedSize(450, 350)

        self.v_main_lay=QVBoxLayout()


        self.title_input=QLineEdit()
        self.title_input.setMinimumWidth(250)
        self.director_input=QLineEdit()
        self.director_input.setMinimumWidth(250)
        self.year_input=QLineEdit()
        self.year_input.setMinimumWidth(250)
        self.genre_input=QLineEdit()
        self.genre_input.setMinimumWidth(250)

        self.add_button=QPushButton("Qo'shish")
        self.add_button.clicked.connect(self.qoshish)

        self.form=QFormLayout()

        self.form.addRow("Film nomi:", self.title_input)
        self.form.addRow("Rejissor:", self.director_input)
        self.form.addRow("Yili:", self.year_input)
        self.form.addRow("Janr:", self.genre_input)
        self.v_main_lay.addLayout(self.form)
        self.v_main_lay.addWidget(self.add_button)
        self.setLayout(self.v_main_lay)

      
    
     




    def qoshish(self):
        self.name=self.title_input.text()
        self.dir=self.director_input.text()
        self.year=self.year_input.text()
        self.genre=self.genre_input.text()

        self.title_input.clear()
        self.director_input.clear()
        self.year_input.clear()
        self.genre_input.clear()

        if self.name and self.dir and self.year and self.genre:
            if self.year.isdigit():
                self.dct={}
                self.dct["name"]=self.name
                self.dct["director"]=self.dir
                self.dct["year"]=self.year
                self.dct["genre"]=self.genre

                try:
                    with open("movies.json", "r+") as f:
                        self.data=json.load(f)
                        f.seek(0)
                        self.data.append(self.dct)
                        json.dump(self.data, f, indent=4)
                        
                except:
                    with open("movies.json", "w") as f:
                        self.data=[]
                        self.data.append(self.dct)
                        json.dump(self.data, f, indent=4)

                        self.title_input.clear()
                        self.director_input.clear()
                        self.year_input.clear()
                        self.genre_input.clear()

                QMessageBox().information(self," ", "Film muvaffaqiyatli qo'shildi")
                    
            else:
                 QMessageBox().warning(self,"ogohlantirish", "Yil raqam bolishi kerak.")

        else:
            QMessageBox().warning(self,"ogohlantirish", "Iltimos barcha ma'lumotlarni to'ldiring")

        
       








app=QApplication([])
win=MyWindow()
win.show()
app.exec_()
