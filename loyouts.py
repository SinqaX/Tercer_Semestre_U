from PySide6.QtWidgets import QApplication ,QWidget, QVBoxLayout, QHBoxLayout,  QPushButton, QLabel, QLineEdit
from PySide6.QtGui import *
import os
import sys

def getWidgetColor(color, texto, color_l="black" ):
    widget = QWidget()
    label = QLabel(texto, widget)

    #obtengo la fuente 
    font = label.font()
    #cambio el tamaño
    font.setPointSize(20)
    #negrita
    font.setBold(True)
    #le asigno la fuente al label
    label.setFont(font)

    
    widget.setAutoFillBackground(True)
    #obtengo la paleta de colores 
    palette = widget.palette()
    #cambiar color
    palette.setColor(QPalette.Window, color)
    palette.setColor(QPalette.WindowText, color_l)
    widget.setPalette(palette)
    widget.setMinimumSize(50,30)
    return widget


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        basedir = os.path.dirname(__file__)
        self.setup_vbox()
        
        
        self.setWindowTitle("Aplicacion con Layouts")


    def setup_vbox(self):

        #creo los widgets
        lbl_num_0 = QLabel("0")
        lbl_num_1 = QLabel("1")
        lbl_num_2 = QLabel("2")
        lbl_num_3 = QLabel("3")

        #creo el tipo de layout este vertical
        vbox = QVBoxLayout()

        #agrego los widgets a el layout
        vbox.addWidget(lbl_num_0)
        vbox.addWidget(lbl_num_1)
        vbox.addWidget(lbl_num_2)
        vbox.addWidget(lbl_num_3)

        #agrego el alyout a la ventana
        self.setLayout(vbox)

    def setup_hbox(self):
        #creo los widgets
        lbl_num_0 = QLabel("0")
        lbl_num_1 = QLabel("1")
        lbl_num_2 = QLabel("2")
        lbl_num_3 = QLabel("3")

        #creo el tipo de layout este horizontal
        hbox = QHBoxLayout()

        #agrego los widgets a el layout
        hbox.addWidget(lbl_num_0)
        hbox.addWidget(lbl_num_1)
        hbox.addWidget(lbl_num_2)
        hbox.addWidget(lbl_num_3)

    def setup_hbox_color(self):
        hbox = QHBoxLayout()
        colores = ["red","blue","yellow","orange"]
        for i in range(4):
            hbox.addWidget(getWidgetColor(colores[i], str(i+1)))
        self.setLayout(hbox)
        


        #agrego el alyout a la ventana
        self.setLayout(hbox)

    def setup_vbox_color(self):
        #creo el tipo de layout este vertical
        vbox = QVBoxLayout()

        #agrego los widgets a el layout
        vbox.addWidget(getWidgetColor("red", "1"))
        vbox.addWidget(getWidgetColor("blue", "2"))
        vbox.addWidget(getWidgetColor("yellow", "3"))
        
        
        #agrego el alyout a la ventana
        self.setLayout(vbox)

    
    



        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())