# from PySide6.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout, QPushButton
# import sys

# class MiVentana(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Ejemplo de valueChanged")
#         self.setGeometry(300, 300, 300, 100)

#         layout = QVBoxLayout()

#         self.progressBar = QProgressBar(self)
#         self.progressBar.setMinimum(0)
#         self.progressBar.setMaximum(100)
#         self.progressBar.setValue(0)

#         button_aumentar = QPushButton("aumentar")
#         button_aumentar.clicked.connect(self.funcion_aumentar)

#         # Conexión de la señal valueChanged a la función actualizarTexto
#         self.progressBar.valueChanged.connect(self.actualizarTexto)

#         layout.addWidget(self.progressBar)
#         layout.addWidget(button_aumentar)
#         self.setLayout(layout)

#     # Función que se llama cada vez que cambia el valor de la barra de progreso
#     def actualizarTexto(self, value):
#         self.setWindowTitle(f"Progreso: {value}%")
    
#     def funcion_aumentar(self):
#         valor = self.progressBar.value() + 10
#         if valor > self.progressBar.maximum():
#             valor = self.progressBar.minimum()
#         self.progressBar.setValue(valor)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ventana = MiVentana()
#     ventana.show()
#     sys.exit(app.exec())
