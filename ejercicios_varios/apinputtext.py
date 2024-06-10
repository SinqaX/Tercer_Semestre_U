from PySide6.QtWidgets import (QApplication, QPushButton, 
                               QWidget,  QLabel, QLineEdit)
from PySide6.QtGui import QMovie, QPixmap
import sys
import os

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Aplicacion con entrada de texto")
        # input = QLineEdit(self)
        # input.setPlaceholderText("ingrese su nombre")# coloca el titulo ingresado en la barra de entrada de fondo
        # # input.setMaxLength(10) limita los caracteres a ingresar en la barra de entrada
        # # input.resize(50, input.size().height()) sirve para ajustar el ancho segun el texto que esta al fondo
        # # input.setReadOnly(True)# no se puede escribir nada
        # input.resize(250,24)#ancho, alto
        # input.move(90,50)

        # #el texto se modifica cuando se hace enter
        # input.returnPressed.connect(lambda: self.return_pressed(input))

        # #el texto seleccinado se muestra en consola
        # input.selectionChanged.connect(lambda:self.selection_changed(input))


        label = QLabel("texto inicial",self)
        label.setGeometry(180,10,100,20)
        input = QLineEdit(self)
        input.resize(250,24)#ancho, alto
        input.move(90,50)
        input.setPlaceholderText("ingrese su nombre")
        
        #este textedited se establece cuando se confirma el cambio
        input.textEdited.connect(label.setText)

        #se conecta el label con el input y lo que se ingrese en input se refleja en el label
        #input.textChanged.connect(label.setText)

        button = QPushButton("poner texto", self)
        button.move(175,100)
        button.clicked.connect(lambda: input.setText("Sin Editar"))



    def return_pressed(self, input):
        print("return pressed")
        input.setText("BOOM!")

    def selection_changed(self, input):
        print("selection changed")
        print(f"Texto seleccionado {input.selectedText()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())