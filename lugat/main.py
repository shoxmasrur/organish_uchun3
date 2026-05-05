from PyQt5.QtWidgets import *
from add import Addwindow
from search import SearchWindow
from list import ListWindow


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay=QVBoxLayout()
        self.h_main_lay=QHBoxLayout()



        self.btn_add=QPushButton("Add")
        self.btn_add.clicked.connect(self.add)
        self.btn_search=QPushButton("Search")
        self.btn_search.clicked.connect(self.search)

        self.btn_list=QPushButton("List")
        self.btn_list.clicked.connect(self.list)

        self.btn_exit=QPushButton("Exit")
        self.btn_exit.clicked.connect(exit)


        self.v_main_lay.addWidget(self.btn_add)
        self.v_main_lay.addWidget(self.btn_search)
        self.v_main_lay.addWidget(self.btn_list)
        self.v_main_lay.addWidget(self.btn_exit)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_main_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)


    def add(self):
        self.hide()
        self.addwindow=Addwindow(self)
        self.addwindow.show()

    def search(self ):
        self.hide()
        self.searchwindow=SearchWindow(self)
        self.searchwindow.show()
    def list(self):
        self.hide()
        self.listwindow=ListWindow(self)
        self.listwindow.show()









app=QApplication([])
win=Mainwindow()

win.show()
app.exec_()