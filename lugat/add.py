import json
from PyQt5.QtWidgets import *


class Addwindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mainwindow=obj

        self.v_main_lay=QVBoxLayout()
        self.btn_lay=QHBoxLayout()

        self.edit_eng=QLineEdit()
        self.edit_eng.setPlaceholderText("eng >>>")

        self.edit_uz=QLineEdit()
        self.edit_uz.setPlaceholderText("uz >>>")

        self.btn_add=QPushButton("add")
        self.btn_add.clicked.connect(self.add)

        self.btn_menu=QPushButton("menu")
        self.btn_menu.clicked.connect(self.menu)

        self.btn_lay.addWidget(self.btn_add)
        self.btn_lay.addWidget(self.btn_menu)

        self.v_main_lay.addWidget(self.edit_eng)
        self.v_main_lay.addWidget(self.edit_uz)
        self.v_main_lay.addLayout(self.btn_lay)

        self.setLayout(self.v_main_lay)


    def add(self):
        
        self.eng=self.edit_eng.text()
        self.uz=self.edit_uz.text()

        f=open("data.json", "r")
        self.data=json.load(f)
        f.close()
        self.msg=QMessageBox()

        if self.eng in self.data:
            self.matn="bunday so'z mavjud"
            self.icon=QMessageBox.Critical
            
        else :
            if self.eng and self.uz:
                self.data[self.eng]=self.uz
                self.matn="Muvafaqiyatli qo'shildi"
                self.icon=QMessageBox.Information
                f=open("data.json", "w")
                json.dump(self.data, f, indent=4)
                f.close()
            else: 
                self.matn="Barcha qatorlarni to'ldiring"
                self.icon=QMessageBox.Critical


        self.msg.setText(self.matn)
        self.msg.setIcon(self.icon)
        self.msg.exec_()

        self.edit_eng.clear()
        self.edit_uz.clear()
            

        
    def menu(self):
        self.hide()
        self.mainwindow.show()

        


    

