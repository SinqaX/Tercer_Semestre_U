from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import Qt
import os
import sys

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("api examen")
        self.setGeometry(50,50,500,350)
        basedir = os.path.dirname(__file__)


        label_photo = QLabel(self)
        label_photo.move(0,0)

        imagen = QPixmap(os.path.join(basedir, "img", "examen.jpg"))
        label_photo.setPixmap(imagen.scaled(500,350))
        
        
        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
