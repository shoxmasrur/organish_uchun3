from PyQt5.QtWidgets import * 

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_lay=QVBoxLayout()

        self.cmb=QComboBox()
        self.cmb.addItems(["Aziz", "Shaxzod", "shoxrux", "Sattor", "Elbek"])
        self.cmb.activated[str].connect(self.test)

        self.main_lay.addWidget(self.cmb)

        self.setLayout(self.main_lay)

    def test(self):

        self.matn=self.cmb.currentText()
        print(self.matn)





app=QApplication([])
win=Mywindow()


win.show()
app.exec_()