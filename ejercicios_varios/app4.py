from PySide6.QtWidgets import (QApplication, QWidget, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap 
import sys

class MainWindow(QWidget):
    
    def __init__(self):

        super().__init__()

        #atributo para colocar titulo
        self.setWindowTitle("aplicacion con label")
        #label para texto en la ventana
        label  = QLabel(self)
        # Obtenemos la fuente actual del QLabel
        font = label.font()

        # Establecemos el tamaño de la fuente en 30 puntos
        font.setPointSize(30)

        # Establecemos la fuente en cursiva
        font.setItalic(True)

        # Aplicamos la fuente modificada al QLabel
        label.setFont(font)

        #label.setAlignment(Qt.aligmentFlag)
        label.setText("Bienvenidos")
        label.setGeometry(100,100,250,40)
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    App.exec()