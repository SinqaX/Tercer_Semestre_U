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
        font = label.font()
        font.setPointSize(30)
        font.setItalic(True)
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