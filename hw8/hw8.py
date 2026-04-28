from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setStyleSheet("background:#333; font-size:30px")
        self.resize(300, 500)


        self.main_layout=QVBoxLayout()
        self.button_layout=QGridLayout()

        self.histryBox=QListWidget()
        self.entryBox=QLineEdit()
        self.entryBox.setStyleSheet('color:white')

        self.main_layout.addWidget(self.histryBox)  
        self.main_layout.addWidget(self.entryBox)
        self.setLayout(self.main_layout)    

        self.button1=QPushButton(text="1", clicked=lambda: self.insertNum('1'))
        self.button2=QPushButton(text="2", clicked=lambda: self.insertNum('2'))
        self.button3=QPushButton(text="3", clicked=lambda: self.insertNum('3'))
        self.button4=QPushButton(text="4", clicked=lambda: self.insertNum('4'))
        self.button5=QPushButton(text="5", clicked=lambda: self.insertNum('5'))
        self.button6=QPushButton(text="6", clicked=lambda: self.insertNum('6'))
        self.button7=QPushButton(text="7", clicked=lambda: self.insertNum('7'))
        self.button8=QPushButton(text="8", clicked=lambda: self.insertNum('8'))
        self.button9=QPushButton(text="9", clicked=lambda: self.insertNum('9'))
        self.button0=QPushButton(text="0", clicked=lambda: self.insertNum('0'))

        self.button_dot=QPushButton(text=".", clicked=lambda: self.insertNum('.'))
        self.button_opr=QPushButton(text="(", clicked=lambda: self.insertNum('('))
        self.button_cpr= QPushButton(text=")", clicked=lambda: self.insertNum(')'))

        self.button_add=QPushButton(text="+", clicked=lambda: self.insertNum('+'))
        self.button_sub=QPushButton(text="-", clicked=lambda: self.insertNum('-'))
        self.button_mult=QPushButton(text="*", clicked=lambda: self.insertNum('*'))
        self.button_div=QPushButton(text="/", clicked=lambda: self.insertNum('/'))

        self.button_calc=QPushButton(text="=", clicked=lambda: self.calculate())
        self.button_clear=QPushButton(text='C', clicked=lambda: self.ClearItems()) 

        
        self.button_layout.addWidget(self.button1, 0,0)
        self.button_layout.addWidget(self.button2, 0,1)
        self.button_layout.addWidget(self.button3, 0,2)
        self.button_layout.addWidget(self.button4, 1,0)
        self.button_layout.addWidget(self.button5, 1,1)
        self.button_layout.addWidget(self.button6, 1,2)
        self.button_layout.addWidget(self.button7, 2,0)
        self.button_layout.addWidget(self.button8, 2,1)
        self.button_layout.addWidget(self.button9, 2,2)
        self.button_layout.addWidget(self.button0, 3,0)

        self.button_layout.addWidget(self.button_dot, 3,1)
          
       


        self.button_layout.addWidget(self.button_add, 0,3)
        self.button_layout.addWidget(self.button_sub, 1,3)
        self.button_layout.addWidget(self.button_mult, 2,3)
        self.button_layout.addWidget(self.button_div, 3,3)


        self.button_layout.addWidget(self.button_clear, 3,1)
        self.button_layout.addWidget(self.button_calc, 3,2)
        


        self.main_layout.addLayout(self.button_layout)


    def insertNum(self, num):
            self.entryBox.insert(num)
    def ClearItems(self):
         self.entryBox.clear()
    def calculate(self):
         self.a=self.entryBox.text()
         self.a=str(self.a)
         self.natija=eval(self.a)
         self.entryBox.setText(str(self.natija))










app=QApplication([])
app.setStyle('fusion')
main=Main()



main.show()
app.exec()

