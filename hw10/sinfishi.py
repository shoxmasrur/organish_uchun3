from PyQt5.QtWidgets import * 
from ikkinchi import boyash

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        

        self.main_lay=QVBoxLayout()


        self.btn_sariq=QPushButton("sariq")
        self.btn_sariq.clicked.connect(lambda: self.test("sariq"))


        self.btn_qizil=QPushButton("qizil")
        self.btn_qizil.clicked.connect(lambda:self.test("qizil"))

        self.main_lay.addWidget(self.btn_qizil)
        self.main_lay.addWidget(self.btn_sariq)

        self.setLayout(self.main_lay)


    def test(self, matn):
        if matn == "sariq":
            self.setStyleSheet("background:yellow")
            self.rang="sariq"
        else:
            self.setStyleSheet("background: red")
            self.rang="qizil"

        self.hide()

        self.ikkinchi_oyna=boyash(self.rang)
        self.ikkinchi_oyna.show()



        
        














app=QApplication([])
win=Mywindow()

win.show()
app.exec_()