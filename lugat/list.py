import json
from PyQt5.QtWidgets import *

class ListWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mainwindow=obj

        self.lbl_lay=QHBoxLayout()
        self.main_lay=QVBoxLayout()

        self.lbl_eng=QLabel("English")
        self.lbl_uz=QLabel("Uzbek")

        with open("data.json", "r") as f:
            self.data=json.load(f)

        self.lst=QListWidget()
        for i, value in self.data.items():
            self.lst.addItem(f"{i}\t   \t{value}")
        self.btn=QPushButton("Menu")
        self.btn.clicked.connect(self.menu)

        self.lbl_lay.addWidget(self.lbl_eng)
        self.lbl_lay.addStretch()
        self.lbl_lay.addWidget(self.lbl_uz)

        self.main_lay.addLayout(self.lbl_lay)
        self.main_lay.addWidget(self.lst)
        self.main_lay.addWidget(self.btn)
        self.setLayout(self.main_lay)



    def menu(self):
        self.hide()
        self.mainwindow.show()