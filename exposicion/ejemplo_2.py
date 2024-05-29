from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import *
import sys

class Ejemplo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo  N° 2")
        self.setGeometry(450,500,350,130)

        #layout principal
        qvbox = QVBoxLayout()


        #se crea el widget qprogressbar
        self.progress = QProgressBar(self)

        #qprogressbar en horizontal
        #self.progress.setOrientation(Qt.Horizontal)

        #formato de texto
        self.progress.setFormat("porcentaje : %p%")

        #por defecto el minimum viene en 0 y el maximum en 100
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)

        #asignar un valor de inicio
        self.progress.setValue(0)

        #boton para aumentar
        button_aumentar = QPushButton("aumentar")
        button_aumentar.clicked.connect(self.funcion_aumentar)

        
        
        #estilos para la barra
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 0px solid #000;
                text-align: center;            }
            QProgressBar::chunk {
                background-color: blue;
                width: 15px;
            }
        """)
        #cambiar fuente de el texto
        self.progress.setFont(QFont("Calculator", 15))

        #centrar la barra
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        qvbox.addWidget(self.progress)
        qvbox.addWidget(button_aumentar)

        self.setLayout(qvbox)

    def funcion_aumentar(self):
        valor = self.progress.value() + 10
        if valor > self.progress.maximum():
            valor = self.progress.minimum()
        self.progress.setValue(valor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ejemplo()
    ventana.show()
    sys.exit(app.exec())



