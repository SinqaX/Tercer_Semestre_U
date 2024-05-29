from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys

class Ejemplo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Métodos Adicionales")
        self.setGeometry(450, 500, 350, 170)

        # Crear la barra QProgressBar
        self.progress = QProgressBar(self)
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(50)
        self.progress.setTextVisible(True)

        # Botones
        button_reset = QPushButton("Reset")
        button_reset.clicked.connect(self.progress.reset)

        button_invert = QPushButton("Invertir Apariencia")
        button_invert.clicked.connect(self.invertirApariencia)

        button_aumentar = QPushButton("Aumentar")
        button_aumentar.clicked.connect(self.aumentarValor)

        button_disminuir = QPushButton("Disminuir")
        button_disminuir.clicked.connect(self.disminuirValor)
        


        #estilos para la barra
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 0px solid #000;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: purple;
                width: 15px;
            }
        """)

        # Layout
        qhbox = QHBoxLayout()
        qhbox.addWidget(button_disminuir)
        qhbox.addWidget(button_aumentar)

        qvbox = QVBoxLayout()

        qvbox.addLayout(qhbox)
        qvbox.addWidget(self.progress)
        qvbox.addWidget(button_reset)
        qvbox.addWidget(button_invert)
    

        self.setLayout(qvbox)


    def invertirApariencia(self):
        #metodo para invertir la barra,   /   este metodo devuelve un booleano y lo invierte con el operador not
        self.progress.setInvertedAppearance(not self.progress.invertedAppearance())

    def aumentarValor(self):
        valor = self.progress.value() + 10
        if valor > self.progress.maximum():
            valor = self.progress.maximum()
        self.progress.setValue(valor)

    def disminuirValor(self):
        valor = self.progress.value() - 10
        if valor < self.progress.minimum():
            valor = self.progress.minimum()
        self.progress.setValue(valor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ejemplo()
    ventana.show()
    sys.exit(app.exec())
