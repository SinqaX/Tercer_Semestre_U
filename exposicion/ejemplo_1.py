from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Ejemplo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo  N° 1")
        self.setGeometry(450,500,350,130)
        
        #crear la barra qprogress
        progress = QProgressBar(self)

        #se le asigna la orientacion, por defecto viene horizontal
        #progress.setOrientation(Qt.Horizontal)

        #se le asigna los valores minimos y maximos, por defecto vienen 0 y 100 respectivamente
        progress.setMinimum(0)
        progress.setMaximum(100)

        #se le asigna un valor a la barra
        progress.setValue(70)

        #se cambia la visibilidad del texto
        progress.setTextVisible(True)#bool

        vbox = QVBoxLayout()
        vbox.addWidget(progress)

        self.setLayout(vbox)
        self.setWindowTitle('Ejemplo  N° 1')

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ejemplo()
    ventana.show()
    sys.exit(app.exec())