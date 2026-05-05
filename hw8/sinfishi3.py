from PyQt5.QtWidgets import * 

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_lay=QVBoxLayout()

        self.lbl=QLabel("Which club is the best?")
        self.lbl.setStyleSheet("font-size:20px")

        self.r1=QRadioButton("bavariya")
        self.r2=QRadioButton("PSJ")
        self.r3=QRadioButton("arsenal")
        self.r4=QRadioButton("real Madrid")
        self.r5=QRadioButton("barselona")
        self.r6=QRadioButton("Inter")

        self.btn=QPushButton("check")
        self.btn.clicked.connect(self.test)

        self.main_lay.addWidget(self.lbl)
        self.main_lay.addWidget(self.r1)
        self.main_lay.addWidget(self.r2)
        self.main_lay.addWidget(self.r3)
        self.main_lay.addWidget(self.r4)
        self.main_lay.addWidget(self.r5)
        self.main_lay.addWidget(self.r6)
        self.main_lay.addWidget(self.btn)

        self.setLayout(self.main_lay)


    def test(self):
        self.msg=QMessageBox()
        self.r5.setStyleSheet("background:green")

        self.r1.setEnabled(False)
        self.r2.setEnabled(False)
        self.r3.setEnabled(False)
        self.r4.setEnabled(False)
        self.r5.setEnabled(False)
        self.r6.setEnabled(False)
        
        if self.r5.isChecked():
            self.matn="To'g'ri javob"
            self.icon=QMessageBox.Information

        else :
            self.matn="Xato javob"
            self.icon=QMessageBox.Critical

        self.msg.setText(self.matn)
        self.msg.setIcon(self.icon)



        self.msg.exec_()



    







app=QApplication([])
win=Mywindow()






win.show()
app.exec_()
