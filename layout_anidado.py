from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import sys    

def getWidgetColor(color, texto, color_l="black"):
    # Se crea un nuevo widget
    widget = QWidget()
    # Se crea una etiqueta (label) con el texto proporcionado, dentro del widget
    label = QLabel(texto, widget)
    # Se obtiene la fuente actual de la etiqueta
    font = label.font()
    # Se establece el tamaño de la fuente a 20 puntos
    font.setPointSize(30)
    # Se aplica la fuente modificada a la etiqueta
    label.setFont(font)

    # Se activa el fondo automático para el widget
    widget.setAutoFillBackground(True)
    # Se obtiene la paleta de colores del widget
    palette = widget.palette()
    # Se establece el color de fondo del widget
    palette.setColor(QPalette.Window, color)
    # Se establece el color del texto de la etiqueta
    palette.setColor(QPalette.WindowText, color_l)
    # Se aplica la paleta modificada al widget
    widget.setPalette(palette)
    # Se establece el tamaño mínimo del widget
    widget.setMinimumSize(50, 30)
    # Se devuelve el widget creado

    return widget
    


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Aplicacion con Layouts Anidados")

        layout_padre = QHBoxLayout()
        layout_hijo_1 = QVBoxLayout()
        layout_hijo_2 = QHBoxLayout()
        layout_hijo_3 = QVBoxLayout()
        #layout_hijo_4 = QHBoxLayout()
        layout_padre.addLayout(layout_hijo_1)
        layout_padre.addLayout(layout_hijo_2)
        layout_padre.addLayout(layout_hijo_3)
        #layout_padre.addLayout(layout_hijo_4)
        
        colores = ["red","blue","yellow","orange","purple","green", "gray"]
        for i in range(3):
            layout_hijo_1.addWidget(getWidgetColor(colores[i], str(i+1)))
        
        layout_hijo_2.addWidget(getWidgetColor(colores[3],"4"))
        
        #espaciado entre los layouts
        #layout_hijo_2.setContentsMargins(10,10,10,10)

        

        
        for i in range(3):
            layout_hijo_3.addWidget(getWidgetColor(colores[i+4], str(i+5)))
            #sin espacios
            #layout_hijo_3.setSpacing(0)

            #con un solo espacio
            if i == 0:
                layout_hijo_3.addSpacing(30)
            layout_hijo_3.setSpacing(0)
            

        self.setLayout(layout_padre)
        





if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
