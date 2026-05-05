from PyQt5.QtWidgets import *


class ThirdWindow(QWidget):
    def __init__(self, obj):
        super().__init__()

        self.secondwindow=obj

        self.main_lay=QVBoxLayout()

        self.btn_main=QPushButton("main")
        self.btn_main.clicked.connect(self.main)

        self.btn_back=QPushButton("back")
        self.btn_back.clicked.connect(self.back)

        self.btn_exit=QPushButton("Exit")
        self.btn_exit.clicked.connect(exit)

        self.main_lay.addWidget(self.btn_back)
        self.main_lay.addWidget(self.btn_main)
        self.main_lay.addWidget(self.btn_exit)
        self.setLayout(self.main_lay)


    def main(self):
        self.hide()
        self.secondwindow.mainwindow.show()
    def back(self):
        self.hide()
        self.secondwindow.show()
    

        

    


class SecondWindow(QWidget):
    def __init__(self, obj):
        super().__init__()

        self.mainwindow=obj
        
        self.setFixedSize(150, 100)

        self.main_lay=QHBoxLayout()

        self.btn_back=QPushButton("back")
        self.btn_back.clicked.connect(self.oldingi)

        self.btn_next=QPushButton("Next")
        self.btn_next.clicked.connect(self.keyingi)

        self.main_lay.addWidget(self.btn_back)
        self.main_lay.addWidget(self.btn_next)
        self.setLayout(self.main_lay)

        


    def oldingi(self):

        self.hide()
        self.mainwindow.show()
    def keyingi(self):
        self.hide()
        self.thirdwindow=ThirdWindow(self)
        self.thirdwindow.show()
        
        



   
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(200,250)

        self.main_lay=QVBoxLayout()


        self.lbl=QLabel("Ketingi oynaga o'tish uchun bosing:")
        self.btn_Next=QPushButton("Next")
        self.btn_Next.clicked.connect(self.test)


        self.main_lay.addWidget(self.lbl)
        self.main_lay.addWidget(self.btn_Next)
        self.setLayout(self.main_lay)


    def test(self):
        self.hide()
        self.secondwindow=SecondWindow(self)
        self.secondwindow.show()












app=QApplication([])
win=MainWindow()

win.show()
app.exec_()