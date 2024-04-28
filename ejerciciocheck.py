# from PySide6.QtWidgets import *
# from PySide6.QtGui import *
# from PySide6.QtCore import *
# import os
# import sys

# class MainWindow(QWidget):

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.check_principal = QCheckBox("todos los colores", self)
#         self.check_principal.setTristate(True)
#         self.check_principal.stateChanged.connect(self.evaluar)

#         self.check_amarillo = QCheckBox("amarillo", self)
#         self.check_azul = QCheckBox("axul", self)
        
#         self.check_rojo = QCheckBox("rojo", self)
        
        
#         layout.addWidget(self.check_principal)
#         layout.addWidget(self.check_amarillo)
#         layout.addWidget(self.check_azul)
#         layout.addWidget(self.check_rojo)


#         self.setLayout(layout)
    

    
#     def evaluar(self, state):

#         if (self.check_amarillo == Qt.CheckState.Checked.value and 
#             self.check_azul == Qt.CheckState.Checked.value and 
#             self.check_rojo == Qt.CheckState.Checked.value):
#             state = Qt.CheckState.Checked.value

#         elif (self.check_amarillo == Qt.CheckState.Checked.value and 
#             self.check_azul == Qt.CheckState.Checked.value):
#             state = Qt.CheckState.PartiallyChecked.value

#         elif (self.check_amarillo == Qt.CheckState.Checked.value and 
#             self.check_rojo == Qt.CheckState.Checked.value):
#             state = Qt.CheckState.PartiallyChecked.value
        
#         elif (self.check_azul == Qt.CheckState.Checked.value and 
#             self.check_rojo == Qt.CheckState.Checked.value):
#             state = Qt.CheckState.PartiallyChecked.value
        
#         else:
#             state = Qt.CheckState.Unchecked.value

            

        



#         # if state == Qt.CheckState.Checked.value:
#         #     self.check_amarillo.setCheckState(Qt.CheckState.Checked)
#         #     self.check_azul.setCheckState(Qt.CheckState.Checked)
#         #     self.check_rojo.setCheckState(Qt.CheckState.Checked)
#         # elif state == Qt.CheckState.Unchecked.value:
#         #     self.check_amarillo.setCheckState(Qt.CheckState.Unchecked)
#         #     self.check_azul.setCheckState(Qt.CheckState.Unchecked)
#         #     self.check_rojo.setCheckState(Qt.CheckState.Unchecked)
        
            


        



# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

#revisar dinamismo del tristate en check principal


from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.check_principal = QCheckBox("Todos los colores")
        self.check_principal.setTristate(True)  # Ahora habilitamos el tristate
        self.check_principal.setChecked(False)

        self.check_amarillo = QCheckBox("Amarillo")
        self.check_azul = QCheckBox("Azul")
        self.check_rojo = QCheckBox("Rojo")

        layout.addWidget(self.check_principal)
        layout.addWidget(self.check_amarillo)
        layout.addWidget(self.check_azul)
        layout.addWidget(self.check_rojo)

        self.setLayout(layout)

        # Conexión de señales
        self.check_principal.clicked.connect(self.toggle_all_colors)
        self.check_amarillo.clicked.connect(self.update_principal_check)
        self.check_azul.clicked.connect(self.update_principal_check)
        self.check_rojo.clicked.connect(self.update_principal_check)

    def update_principal_check(self):
        checked_count = sum([self.check_amarillo.isChecked(),
                             self.check_azul.isChecked(),
                             self.check_rojo.isChecked()])

        if checked_count == 3:
            self.check_principal.setCheckState(Qt.Checked)
        elif checked_count == 0:
            self.check_principal.setCheckState(Qt.Unchecked)
        else:
            self.check_principal.setCheckState(Qt.PartiallyChecked)

    def toggle_all_colors(self):
        checked = self.check_principal.isChecked()
        self.check_amarillo.setChecked(checked)
        self.check_azul.setChecked(checked)
        self.check_rojo.setChecked(checked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

