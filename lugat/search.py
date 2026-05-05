import json
from PyQt5.QtWidgets import *
from add import Addwindow


class SearchWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mainwindow=obj

        self.r_lay=QHBoxLayout()
        self.ebtn_lay=QHBoxLayout()
        self.main_lay=QVBoxLayout()

        self.rbtn_eng=QRadioButton("Eng")
        self.rbtn_eng.setChecked(True)
        self.rbtn_uz=QRadioButton("Uz")

        self.edit=QLineEdit()
        self.btn=QPushButton("Ok")
        self.btn.clicked.connect(self.ok)

        self.lbl=QLabel()

        self.btn_menu=QPushButton("Menu")
        self.btn_menu.clicked.connect(self.menu)

        self.r_lay.addWidget(self.rbtn_eng)
        self.r_lay.addWidget(self.rbtn_uz)

        self.ebtn_lay.addWidget(self.edit)
        self.ebtn_lay.addWidget(self.btn)

        self.main_lay.addLayout(self.r_lay)
        self.main_lay.addLayout(self.ebtn_lay)
        self.main_lay.addWidget(self.lbl)
        self.main_lay.addWidget(self.btn_menu)
        self.setLayout(self.main_lay)


    def ok (self):
        self.count=0
        with open("data.json", "r") as self.f:
            self.data=json.load(self.f)
        self.word=self.edit.text()

        if self.rbtn_eng.isChecked():
            if self.word in self.data:
                self.lbl.setText(self.data[self.word])
            else :
                self.msg=QMessageBox()
                self.msg.setText("Bunday so'z yoq qo'shishni xoxlaysizmi")
                self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                self.msg.buttonClicked.connect(self.test)
                self.msg.exec_()
        else:
            for i,value in self.data.items():
                if self.word==value:
                    self.lbl.setText(i)
                    break
            else:
                    self.msg=QMessageBox()
                    self.msg.setText("Bunday so'z yoq qo'shishni xoxlaysizmi")
                    self.msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                    self.msg.buttonClicked.connect(self.test)
                    self.msg.exec_()
        
        



    def test(self, matn):

        if matn.text()=="&Yes":

            self.addwindow=Addwindow(self)
            self.hide()
            self.addwindow.show()
            
    def menu(self):
        self.hide()
        self.mainwindow.show()
        
            






