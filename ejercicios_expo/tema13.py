from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import sys

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
