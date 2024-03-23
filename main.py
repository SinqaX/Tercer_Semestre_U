from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox
from PySide6.QtGui import QPixmap

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()

    def generar_contenido(self):
        label  = QLabel(self)
        image_path = QPixmap("C:/Users/SEBASTIAN/OneDrive/Documentos/GitHub/Tercer_Semestre_U/img/mono.jpg")
        label.setPixmap(image_path)
        label.resize(label.sizeHint())