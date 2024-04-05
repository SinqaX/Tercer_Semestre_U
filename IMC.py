from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout
from PySide6.QtGui import QFont, QIcon
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        basedir = os.path.dirname(__file__)

        self.setWindowTitle("Calculadora IMC")

        
        
        imc = QLabel(self)
        imc.setText("IMC =>")
        imc.setFont(QFont("Arial", 10))
        imc.move(10,20)

        self.input_imc = QLineEdit(self)
        self.input_imc.setPlaceholderText("No calculado")
        self.input_imc.setFont(QFont("Arial", 10))
        self.input_imc.setGeometry(80,10,205,30)
        self.input_imc.setReadOnly(True)

        genero = QLabel(self)
        genero.setText("Genero:")
        genero.setFont(QFont("Arial", 10))
        genero.move(10,55)

        self.input_genero = QLineEdit(self)
        self.input_genero.setPlaceholderText("M / F")
        self.input_genero.setFont(QFont("Arial", 10))
        self.input_genero.setGeometry(80,45,205,30)
        self.input_genero.setMaxLength(1)

        altura = QLabel(self)
        altura.setText("Altura:")
        altura.setFont(QFont("Arial", 10))
        altura.move(10,90)

        self.input_altura = QLineEdit(self)
        self.input_altura.setPlaceholderText("Metros")
        self.input_altura.setFont(QFont("Arial", 10))
        self.input_altura.setGeometry(80,80,205,30)

        peso = QLabel(self)
        peso.setText("Peso:")
        peso.setFont(QFont("Arial", 10))
        peso.move(10,125)

        self.input_peso = QLineEdit(self)
        self.input_peso.setPlaceholderText("Kilogramos")
        self.input_peso.setFont(QFont("Arial", 10))
        self.input_peso.setGeometry(80,115,205,30)

        button_calcular = QPushButton(self)
        button_calcular.setText("Calcular")
        button_calcular.setGeometry(10,150,275,30)
        button_calcular.clicked.connect(self.calcular_imc)

    def calcular_imc(self):
        try:
            altura = float(self.input_altura.text())
            peso = float(self.input_peso.text())
            genero = self.input_genero.text().upper()


            if altura > 0 and peso > 0:
                imc = peso / (altura ** 2) 

                # Evaluar el IMC
                if genero == "M":
                    if imc < 20:
                        estado = "Desnutrición"
                    elif 20 <= imc < 25:
                        estado = "Normalidad"
                    elif 25 <= imc < 30:
                        estado = "Sobrepeso"
                    elif 30 <= imc < 40:
                        estado = "Obesidad"
                    else:
                        estado = "Obesidad Grave"
                elif genero == "F":
                    if imc < 19:
                        estado = "Desnutrición"
                    elif 19 <= imc < 24:
                        estado = "Normalidad"
                    elif 24 <= imc < 28:
                        estado = "Sobrepeso"
                    elif 28 <= imc < 32:
                        estado = "Obesidad"
                    else:
                        estado = "Obesidad Grave"
                else:
                    if genero not in ["M", "F"]:
                        imc = peso / (altura ** 2)  
                        return self.input_imc.setText(f" {imc:.2f} - N/D")
                

                self.input_imc.setText(f"{imc:.2f} - {estado}")
            else:
                self.input_imc.setText("Datos inválidos")
        except ValueError:
            self.input_imc.setText("Datos inválidos")
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
