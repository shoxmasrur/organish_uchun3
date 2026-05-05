from PyQt5.QtWidgets import * 

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_lay=QVBoxLayout()
        self.btn_lay=QHBoxLayout()


        self.lbl=QLabel("Mashina Bozor")
        self.lbl.setStyleSheet("font-size:20px")
        
        self.c1=QCheckBox("Matiz     -  40000")
        self.c2=QCheckBox("Nexia     -  60000")
        self.c3=QCheckBox("damas     -  80000")
        self.c4=QCheckBox("cobolt    -  120000")
        self.c5=QCheckBox("Gentra    -  140000")
        self.c6=QCheckBox("Tico      -   20000")

        self.lst=[self.c1, self.c2, self.c3, self.c4, self.c5, self.c6]

        self.btn_ok=QPushButton("ok")
        self.btn_ok.clicked.connect(self.ok)

        self.btn_back=QPushButton("back")
        self.btn_back.clicked.connect(self.back)

        self.btn_back.hide()
        self.btn_buy=QPushButton("buy")
        self.btn_buy.clicked.connect(self.buy)


        self.btn_buy.hide()
        self.btn_exit=QPushButton("exit")



        self.btn_lay.addWidget(self.btn_back)
        self.btn_lay.addWidget(self.btn_ok)
        self.btn_lay.addWidget(self.btn_buy)
        self.btn_lay.addWidget(self.btn_exit)

        self.main_lay.addWidget(self.lbl)

        for i in self.lst:
            self.main_lay.addWidget(i)
            i.setStyleSheet("font-size: 20px")

        self.main_lay.addLayout(self.btn_lay)

        self.setLayout(self.main_lay)

    def ok(self):
        self.sum=0
        for i in self.lst:
            if i.isChecked():
              self.sum += int(i.text().split()[-1])
        for i in self.lst:
            i.hide()
        self.btn_buy.show()
        self.btn_back.show()

        self.lbl.setText(f"sizdan {self.sum}")

    def back(self):
        

     self.lbl.setText("Mashina bozor")
     for i in self.lst:
        i.show()
        i.setChecked(False)

        self.btn_buy.hide()
        self.btn_back.hide()

    def buy(self):
       self.msg=QMessageBox()
       self.msg.setText("Haridingiz uchun raxmat")
       self.msg.Icon(QMessageBox.Information)
       self.back()


       self.msg.exec_()

       



        







app=QApplication([])
win=Mywindow()

win.show()
app.exec_()