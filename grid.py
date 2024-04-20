from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import sys

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle("My App")

        
        # layout_padre = QVBoxLayout()
        # layout_botones = QGridLayout()
        
        #politicas de creciemito para los botones

        # button1 = QPushButton("1,1",self)
        # button2 = QPushButton("1,2",self)
        # button3 = QPushButton("2,1",self)
        # button4 = QPushButton("2,2",self)
        # button5 = QPushButton("3,3",self)
        # button5.setSizePolicy()

        # layout_botones.addWidget(button1,1,1)
        # layout_botones.addWidget(button2,1,2)
        # layout_botones.addWidget(button3,3,1)
        # layout_botones.addWidget(button4,3,2)
        # layout_botones.addWidget(button5,2,3)

        #forma normal de crear esta forma de formato

        # label1 = QLabel("Name:", self)
        # label2 = QLabel("Email:", self)
        # label3 = QLabel("Age:", self)

        # lineedit1 = QPushButton(self)
        # lineedit2 = QPushButton(self)
        # lineedit3 = QPushButton(self)


        # layout_botones.addWidget(label1,0,0)
        # layout_botones.addWidget(label2,1,0)
        # layout_botones.addWidget(label3,2,0)

        # layout_botones.addWidget(lineedit1,0,1,1,2)
        # layout_botones.addWidget(lineedit2,1,1,1,2)
        # layout_botones.addWidget(lineedit3,2,1,1,2)

        # layout_padre.addLayout(layout_botones)
        # self.setLayout(layout_padre)

        self.setup_stacked()


    def setup_form(self):
        #colocar filas de widgets
        form = QFormLayout()
        form.addRow("Name:", QLineEdit())
        form.addRow("Email:", QLineEdit())
        form.addRow("Age:", QLineEdit())
        self.setLayout(form)
    
    def setup_stacked(self):
        #colocar varios widgets encima 
        stack = QStackedLayout()

        lay_v = QVBoxLayout()

        btn1 = QPushButton("1", self)
        btn2 = QPushButton("2", self)
        btn3 = QPushButton("3", self)

        # btn1.clicked.connect(lambda: stack.setCurrentWidget(btn2))
        # btn2.clicked.connect(lambda: stack.setCurrentWidget(btn3))
        # btn3.clicked.connect(lambda: stack.setCurrentWidget(btn1))

        lay_v.addWidget(btn1)
        lay_v.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(lay_v)

        btn1.clicked.connect(lambda: stack.setCurrentIndex(1))
        btn2.clicked.connect(lambda: stack.setCurrentIndex(1))
        btn3.clicked.connect(lambda: stack.setCurrentIndex(0))

        stack.addWidget(widget)
        stack.addWidget(btn3)


        self.setLayout(stack)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

        
        
