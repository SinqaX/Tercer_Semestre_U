from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys
from random import choice

window_titles = ["mi aplicacion", "tu aplicacion", "que demonios", "pedrito que te pasa", "algo salio mal"]

#subclase que qqwidget que se pude personalizar la ventana 
class MainWindow(QWidget):
    
    def __init__(self):

        super().__init__()

        #atributo para colocar titulo
        self.setWindowTitle("aplicacion con boton")
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.button = QPushButton("Press Me!", self)
        self.button.setGeometry(300,30,80,23)
        self.button.setParent(self)
        self.button.setStyleSheet("background-color: black; color: white;")
        self.button.clicked.connect(lambda  : self.presionaElBoton(self.button))
        self.button.resize(self.button.sizeHint())

    def presionaElBoton(self, button):
        self.setWindowTitle(choice(window_titles))
        button.setText("me has presionado pedrito!")
        button.resize(button.sizeHint().width(), button.sizeHint().height())

    def the_window_title_changed(self, window_title,button):
        if window_title == "algo salio mal":
            self.button.setDisabled(True)
            


app = QApplication(sys.argv)

#se crea la ventana
window = MainWindow()

#se llama a la ventana
window.show()
app.exec()
