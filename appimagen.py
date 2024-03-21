from PySide6.QtWidgets import (QApplication, QWidget, QLabel)
from PySide6.QtGui import QPixmap, QMovie
import sys
import os
class MainWindow(QWidget):
    
    def __init__(self):

        super().__init__()

        #atributo para colocar titulo
        self.setWindowTitle("aplicacion con imagen")
        #label para texto en la ventana
        label  = QLabel(self)
        #imagen
        # imagen = QPixmap("C:\\Users\\SEBASTIAN\\OneDrive\\Escritorio\\mono.jpg")
        # label.setPixmap(imagen)
        # label.resize(label.sizeHint())
        movie = QMovie("C:\\Users\\SEBASTIAN\\OneDrive\\Escritorio\\giphy (1).gif")  # Cambia "ruta/al/archivo.gif" por la ruta de tu archivo GIF
        label.setMovie(movie)
        movie.start()
        label.resize(label.sizeHint())
        
        

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print("ruta actual : ", os.getcwd())
    App.exec()