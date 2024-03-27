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
# Obtiene el directorio base del archivo de script actual
        basedir = os.path.dirname(__file__) 
# Carga la imagen "mono.png" ubicada en el directorio "img"
        imagen = QPixmap(os.path.join(basedir,"img","mono.png"))  
# Establece la imagen en el QLabel
        label.setPixmap(imagen)  
# Ajusta el tamaño del QLabel al tamaño de la imagen
        label.resize(label.sizeHint())  

        #Gif
# Carga el archivo GIF "giphy (1).gif" ubicado en el directorio "img"
        movie = QMovie(os.path.join(basedir, "img","giphy (1).gif"))  
# Establece el archivo GIF como la película en el QLabel        
        label.setMovie(movie)  
# Inicia la reproducción de la película GIF
        movie.start()  
# Ajusta el tamaño del QLabel al tamaño del GIF
        label.resize(label.sizeHint())  

        
        

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print("ruta actual : ", os.getcwd())
    App.exec()