import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader



def mainwindow_setup(w):

    w.setWindowTitle("Ejercicio Jp")
    # Conectar señales directamente después de cargar la interfaz
    button_convertidor = window.findChild(QtWidgets.QPushButton, "button_convertidor_4")
    entrada_numero = window.findChild(QtWidgets.QLineEdit, "entrada_numero_4")
    lista_widget = window.findChild(QtWidgets.QListWidget, "lista_widget_4")

    radio_binario = window.findChild(QtWidgets.QRadioButton, "Binario_4")
    radio_octal = window.findChild(QtWidgets.QRadioButton, "Octal_4")
    radio_hexadecimal = window.findChild(QtWidgets.QRadioButton, "Hexadecimal_4")
    radio_decimal = window.findChild(QtWidgets.QRadioButton, "Decimal_4")
    
    radio_decimal.setChecked(True)

    def convert_number():
        lista_widget.clear()
        numero_l = entrada_numero.text().strip()
        if entrada_numero is not None and lista_widget is not None:

            try:
                if numero_l:
                    numero = int(numero_l)
                    if radio_decimal.isChecked():
                        lista_widget.clear()
                        lista_widget.addItem(f"{numero}")
                    elif radio_binario.isChecked():
                        lista_widget.clear()
                        lista_widget.addItem(f"{bin(numero)[2:]}")
                    elif radio_octal.isChecked():
                        lista_widget.clear()
                        lista_widget.addItem(f"{oct(numero)[2:]}")
                    elif radio_hexadecimal.isChecked():
                        lista_widget.clear()
                        lista_widget.addItem(f"{hex(numero)[2:].upper()}")
                    else:
                        lista_widget.clear()
                        lista_widget.addItem("Error")
                else:
                    lista_widget.clear()
                    lista_widget.addItem("Error")
            except ValueError:
                lista_widget.clear()
                lista_widget.addItem("Error")
        else:
            print("No se encontraron los widgets necesarios.")

    if button_convertidor is not None:
        button_convertidor.clicked.connect(convert_number)
    


if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Tercer_Semestre_U\\ejercicios_expo\\ejercicio4.ui", None)
    mainwindow_setup(window)
    window.show()
    app.exec()
