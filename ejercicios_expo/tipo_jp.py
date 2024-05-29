from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ejercicio4_ui import Ui_MainWindow #En 'tu_archivo', se debe reemplazar el nombre del archivo
                               #ui generado de Qt Designer que se convirtió a .py desde el terminal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Decimal_4.setChecked(True)
        self.ui.button_convertidor_4.clicked.connect(self.convertidor)
    
    def convertidor(self):
        self.ui.pantalla.display(0)
        numero = self.ui.entrada_numero_4.text().strip()
        if numero and numero.isdigit():
            if self.ui.Decimal_4.isChecked():
                self.ui.pantalla.display(numero)
            elif self.ui.Binario_4.isChecked():
                self.ui.pantalla.display(f"{bin(int(numero))[2:]}")
            elif self.ui.Octal_4.isChecked():
                self.ui.pantalla.display(f"{oct(int(numero))[2:]}")
            elif self.ui.Hexadecimal_4.isChecked():
                self.ui.pantalla.display(f"{hex(int(numero))[2:]}")
        else:
            self.ui.pantalla.display("Error")



                

    #Espacio para la lógica del código, recuerda el nombre de las variables de los objetos
    #serán los mismos que se usarán acá 

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()