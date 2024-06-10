from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtCore
import math
import os
import sys

# problemas con el promedio
# elevacion volverla mas dinamica
#controlar division /0

def apply_dark_theme(app):
    # Define el estilo CSS para el tema oscuro
    

    estilos_buttons = """
        QLabel {
        font-family: Verdana;
        }
        QPushButton {
            height: 50px;
            width: 50px;
            font-size: 20px;
            font-family: Verdana;
            border-radius: 5px;
            background-color: #ffffff;      
        }

        QPushButton:hover {
            background-color: #E1E1E1;  
        }
        """
    # Aplica el estilo CSS a la aplicación
    app.setStyleSheet(estilos_buttons)


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        basedir = os.path.dirname(__file__)
        
        layout_padre = QVBoxLayout()
        layout_botones = QGridLayout()

        self.input_line = QLineEdit(self)
        #self.input_line.setGeometry(5, 5, 212, 125)
        
        self.input_line.setFont(QFont("Arial", 35))
        self.input_line.setStyleSheet("border: none;")
        # self.input_line.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.input_line.setAlignment(QtCore.Qt.AlignmentFlag(10))
        self.input_line.setReadOnly(True)  # Deshabilita la edición directa
        layout_padre.addWidget(self.input_line)

        self.setWindowTitle("Calculadora")
        Icon = QIcon(os.path.join(basedir,"img","icon.png"))
        self.setWindowIcon(Icon)
        

        label = QLabel(self)
        label.resize(label.sizeHint())
        
        

        # button1 = QPushButton(self)
        # button1.setFont(QFont("Arial", 12))
        # button1.setText("1")
        # button1.clicked.connect(lambda: self.append_text("1"))
        # layout_botones.addWidget(button1,6,2)

        # button2 = QPushButton(self)
        # button2.setFont(QFont("Arial", 12))
        # button2.setText("2")
        # button2.clicked.connect(lambda: self.append_text("2"))
        # layout_botones.addWidget(button2,6,3)

        # button3 = QPushButton(self)
        # # button3.setGeometry(112,300,50,50)
        # button3.setFont(QFont("Arial", 12))
        # button3.setText("3")
        # button3.clicked.connect(lambda: self.append_text("3"))
        # layout_botones.addWidget(button3,6,4)
        
        # button4 = QPushButton(self)
        # # button4.setGeometry(5,245,50,50)
        # button4.setFont(QFont("Arial", 12))
        # button4.setText("4")
        # button4.clicked.connect(lambda: self.append_text("4"))
        # layout_botones.addWidget(button4,5,2)

        # button5 = QPushButton(self)
        # # button5.setGeometry(60,245,50,50)
        # button5.setFont(QFont("Arial", 12))
        # button5.setText("5")
        # button5.clicked.connect(lambda: self.append_text("5"))
        # layout_botones.addWidget(button5,5,3)

        # button6 = QPushButton(self)
        # # button6.setGeometry(112,245,50,50)
        # button6.setFont(QFont("Arial", 12))
        # button6.setText("6")
        # button6.clicked.connect(lambda: self.append_text("6"))
        # layout_botones.addWidget(button6,5,4)

        # button7 = QPushButton(self)
        # # button7.setGeometry(5,190,50,50)
        # button7.setFont(QFont("Arial", 12))
        # button7.setText("7")
        # button7.clicked.connect(lambda: self.append_text("7"))
        # layout_botones.addWidget(button7,4,2)

        # button8 = QPushButton(self)
        # # button8.setGeometry(60,190,50,50)
        # button8.setFont(QFont("Arial", 12))
        # button8.setText("8")
        # button8.clicked.connect(lambda: self.append_text("8"))
        # layout_botones.addWidget(button8,4,3)

        # button9 = QPushButton(self)
        # # button9.setGeometry(112,190,50,50)
        # button9.setFont(QFont("Arial", 12))
        # button9.setText("9")
        # button9.clicked.connect(lambda: self.append_text("9"))
        # layout_botones.addWidget(button9,4,4)


        # button0 = QPushButton(self)
        # # button0.setGeometry(60, 355, 50, 50)
        # button0.setFont(QFont("Arial", 12))
        # button0.setText("0")
        # button0.clicked.connect(lambda: self.append_text("0"))
        # layout_botones.addWidget(button0,7,2)

        # # Operator buttons
        # button_suma = QPushButton(self)
        # # button_suma.setGeometry(170, 300, 50, 50)
        # button_suma.setFont(QFont("Arial", 12))
        # button_suma.setText("+")
        # button_suma.clicked.connect(lambda: self.append_text("+"))
        # layout_botones.addWidget(button_suma,7,5)
        

        # button_resta = QPushButton(self)
        # # button_resta.setGeometry(170, 245, 50, 50)
        # button_resta.setFont(QFont("Arial", 12))
        # button_resta.setText("-")
        # button_resta.clicked.connect(lambda: self.append_text("-"))
        # layout_botones.addWidget(button_resta,6,5)

        # button_mult = QPushButton(self)
        # # # button_mult.setGeometry(170, 190, 50, 50)
        # button_mult.setFont(QFont("Arial", 12))
        # button_mult.setText("*")
        # button_mult.clicked.connect(lambda: self.append_text("*"))
        # layout_botones.addWidget(button_mult,5,5)

        # button_div = QPushButton(self)
        # # button_div.setGeometry(170, 135, 50, 50)
        # button_div.setFont(QFont("Arial", 12))
        # button_div.setText("/")
        # button_div.clicked.connect(lambda: self.append_and_calculate_division("/"))
        # layout_botones.addWidget(button_div,4,5)

        # button_decimal = QPushButton(self)
        # # button_decimal.setGeometry(112, 355, 50, 50)
        # button_decimal.setFont(QFont("Arial", 12))
        # button_decimal.setText(".")
        # button_decimal.clicked.connect(lambda: self.append_text("."))
        # layout_botones.addWidget(button_decimal,7,3)

        # button_equal = QPushButton(self)
        # # button_equal.setGeometry(170, 355, 50, 50)
        # button_equal.setFont(QFont("Arial", 12))
        # button_equal.setText("=")
        # button_equal.setStyleSheet("height : 110px")
        # button_equal.clicked.connect(self.calculate)
        # layout_botones.addWidget(button_equal,6,6,2,1)

        
        # # button_clear_entry = QPushButton(self)
        # # # button_clear_entry.setGeometry(5, 135, 50, 50)
        # # button_clear_entry.setFont(QFont("Arial", 12))
        # # button_clear_entry.setText("CE")
        # # button_clear_entry.clicked.connect(self.clear_entry)

        # button_clear_all = QPushButton(self)
        # # button_clear_all.setGeometry(60, 135, 50, 50)
        # button_clear_all.setFont(QFont("Arial", 12))
        # button_clear_all.setText("C")
        # layout_botones.addWidget(button_clear_all,3,2)

        # button_porcentaje = QPushButton(self)
        # # button_porcentaje.setGeometry(5,355,50,50)
        # button_porcentaje.setText("%")
        # button_porcentaje.setFont(QFont("Arial", 12))
        # layout_botones.addWidget(button_porcentaje,7,4)

        # button_potencia = QPushButton(self)
        # # button_potencia.setGeometry(112,135,50,50)
        # button_potencia.setFont(QFont("Arial", 12))
        # button_potencia.setText("^2")
        # button_potencia.clicked.connect(self.calculate_pow)
        # layout_botones.addWidget(button_potencia,5,6)

        # button_raiz = QPushButton(self)
        # button_raiz.setFont(QFont("Arial", 12))
        # button_raiz.setText("√")
        
        # layout_botones.addWidget(button_raiz,4,6)

        # button_pi = QPushButton(self)
        # button_pi.setFont(QFont("Arial", 12))
        # button_pi.setText("π")
        
        # layout_botones.addWidget(button_pi,3,6)

        # button_mod = QPushButton(self)
        # button_mod.setFont(QFont("Arial", 12))
        # button_mod.setText("mod")
       
        # layout_botones.addWidget(button_mod,3,5)

        # button_pa = QPushButton(self)
        # button_pa.setFont(QFont("Arial", 12))
        # button_pa.setText(")")
        # layout_botones.addWidget(button_pa,3,4)
       
        # button_pare = QPushButton(self)
        # button_pare.setFont(QFont("Arial", 12))
        # button_pare.setText("(")
        # layout_botones.addWidget(button_pare,3,3)

        # button_clear_all.clicked.connect(self.clear_all)
        # button_porcentaje.clicked.connect(self.calculate_mod)
        # button_potencia.clicked.connect(self.calculate_pow)
        # button_raiz.clicked.connect(self.calculate_raiz)
        # button_pi.clicked.connect(self.calculate_pi)
        # button_mod.clicked.connect(self.calculate_mod)
        # button_pa.clicked.connect(lambda: self.append_text(")"))
        # button_pare.clicked.connect(lambda: self.append_text("("))

        # # Agregar el layout de botones al layout principal
        # layout_padre.addLayout(layout_botones)
        # self.setLayout(layout_padre)

    
        button_positions = [
            ('1', (6, 2)), ('2', (6, 3)), ('3', (6, 4)),
            ('4', (5, 2)), ('5', (5, 3)), ('6', (5, 4)),
            ('7', (4, 2)), ('8', (4, 3)), ('9', (4, 4)),
            ('0', (7, 2)), ('+', (7, 5)), ('-', (6, 5)),
            ('*', (5, 5)), ('/', (4, 5)), ('.', (7, 3)),
            ('C', (3, 2)), ('%', (7, 4)),
            ('^2', (5, 6)), ('√', (4, 6)), ('π', (3, 6)),
            ('mod', (3, 5)), (')', (3, 4)), ('(', (3, 3))
        ]

        layout_botones = QGridLayout()

        for text, pos in button_positions:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 12))
            layout_botones.addWidget(button, *pos)

        layout_padre.addLayout(layout_botones)
        self.setLayout(layout_padre)
    
        button_equal = QPushButton(self)
        # button_equal.setGeometry(170, 355, 50, 50)
        button_equal.setFont(QFont("Arial", 12))
        button_equal.setText("=")
        button_equal.setStyleSheet("height : 110px")
        button_equal.clicked.connect(self.calculate)
        layout_botones.addWidget(button_equal,6,6,2,1)

    
    def calculate_raiz(self):
        expression = self.input_line.text()
        try:
            result = math.sqrt(eval(expression))
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def calculate_pi(self):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + "π")

    def append_text(self, text):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + text)
        self.input_line.textChanged.connect(self.update_font_size)

    def calculate(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def clear_entry(self):
        current_text = self.input_line.text()
        self.input_line.setText(current_text[:-1])

    def clear_all(self):
        self.input_line.clear()

    def calculate_mod(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            result = result / 100  # Calcula el porcentaje
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def calculate_pow(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            result = math.pow(result, 2)  # Calcula el cuadrado
            self.input_line.setText(str(result))
        except Exception as e:
            print("Error:", e)

    def append_and_calculate_division(self, text):
        current_text = self.input_line.text()
        self.input_line.setText(current_text + text)
        self.calculate_division()

    def calculate_division(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
        except ZeroDivisionError:
            self.input_line.setText("/0 no soportada")
        except Exception as e:
            print("Error:", e)
    
    def update_font_size(self):
        text_length = len(self.input_line.text())
        font_size = max(35 - (text_length // 5) * 5, 12)
        font = QFont("Arial", font_size)
        self.input_line.setFont(font)

    
    

if __name__ == "__main__":
    app = QApplication([])
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


