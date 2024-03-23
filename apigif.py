from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QMovie, QPixmap
import sys
import os

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        basedir = os.path.dirname(__file__)
        
        # Crear el layout principal
        layout = QVBoxLayout(self)
        
        # Añadir título a la ventana
        self.setWindowTitle("Aplicación con GIF")
        
        # Crear QLabel para mostrar el GIF
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Cargar el GIF
        self.movie = QMovie(os.path.join(basedir, "img", "giphy (1).gif")) 
        self.movie.jumpToFrame(0)  # Establece el primer cuadro del GIF como la imagen estática
        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)  # Escalar el contenido de la etiqueta al tamaño del GIF
        self.label.setFixedSize(400, 300)

        # Botón para detener la animación
        self.stop_button = QPushButton("Detener", self)
        self.stop_button.clicked.connect(self.stop_animation)
        layout.addWidget(self.stop_button)

        # Botón para iniciar la animación
        self.start_button = QPushButton("Iniciar", self)
        self.start_button.clicked.connect(self.start_animation)
        layout.addWidget(self.start_button)

    def stop_animation(self):
        self.movie.stop()

    def start_animation(self):
        self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
