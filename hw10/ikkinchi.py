from PyQt5.QtWidgets import *


class boyash(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.birinchi_oyna=obj


        self.main_lay=QHBoxLayout()

        self.btn_back=QPushButton("back")
        self.btn_back.clicked.connect(self.back)

        self.btn_exit=QPushButton("Exit")

        self.main_lay.addWidget(self.btn_back)
        
        self.main_lay.addWidget(self.btn_exit)

        self.setLayout(self.main_lay)

    def back(self):

        self.birinchi_oyna.show()   
        self.hide()     












app=QApplication([])
win=boyash()

win.show()
app.exec_()

