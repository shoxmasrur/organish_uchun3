from PyQt5.QtWidgets import *


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_lay=QVBoxLayout()
        self.btn_lay=QHBoxLayout()

        self.lbl=QLabel("Mashina bozor")

        self.edit=QLineEdit()
        self.edit.setPlaceholderText("mashina nomi>>>")

        self.btn=QPushButton("Buy")
        self.btn.clicked.connect(self.test)


        self.btn_lay.addStretch()
        self.btn_lay.addWidget(self.btn)
        self.btn_lay.addStretch()

        self.main_lay.addWidget(self.lbl)
        self.main_lay.addWidget(self.edit)
        self.main_lay.addLayout(self.btn_lay)

        self.setLayout(self.main_lay)

        self.royhat={
            "matiz":5,
            "Nexia":19,
            "Gentra":30,
            "Tico":3,
            "damas":60,
            "cobolt":23
        }


    def test(self):

        self.car=self.edit.text()
        self.msg=QMessageBox()
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.buttonClicked.connect(self.yangi)

        if self.car in self.royhat:
            self.matn="Xaridingiz uchun raxmat"
            self.icon=QMessageBox.Information

            self.royhat[self.car]-=1
            print(self.royhat[self.car])
        else:
            self.matn="Bu mashina bizda yoq"
            self.icon=QMessageBox.Critical


        self.msg.setText(self.matn)
        self.msg.setIcon(self.icon)



        self.msg.exec_()

    def yangi(self, obj):

        if obj.text()== "&Yes":
            self.setStyleSheet("background: black")
        else:
            self.setStyleSheet("background:green")

    
        
        








app=QApplication([])
win=Mywindow()

win.show()
app.exec_()