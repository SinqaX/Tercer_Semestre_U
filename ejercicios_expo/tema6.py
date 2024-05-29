from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os

class calculoProm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("calculador de promedios")

        qhbox = QHBoxLayout(self)

        self.frame_izq = QFrame()
        self.frame_der = QFrame()

        qhbox.addWidget(self.frame_izq, 99)
        qhbox.addWidget(self.frame_der, 1)

        self.setLayout(qhbox)
        self.frame_izquierdo()
        self.frame_derecho()

    def frame_izquierdo(self):
        qvbox = QVBoxLayout()

        form = QFormLayout()
        self.nombre = QLineEdit()
        form.addRow("Nombre", self.nombre)

        qhbox_spin = QHBoxLayout()
        form_edad = QFormLayout()
        self.spin_edad = QSpinBox()
        self.spin_edad.setRange(0,100)
        form_edad.addRow("Edad", self.spin_edad)
        form_grado = QFormLayout()
        self.spin_grado = QSpinBox()
        self.spin_grado.setRange(9,11)
        form_grado.addRow("Grado", self.spin_grado)
        qhbox_spin.addLayout(form_edad)
        qhbox_spin.addLayout(form_grado)

        self.combo = QComboBox()

        self.button_registrar = QPushButton("Registrar Estudiante")

        self.button_borrar = QPushButton("Borrar Estudiante")

        self.prom_9 = "N/A"
        self.label_promedio_9 = QLabel(f"Promedio de 9no : {self.prom_9}")

        self.prom_10 = "N/A"
        self.label_promedio_10 = QLabel(f"Promedio de 10mo : {self.prom_10}")

        self.prom_11 = "N/A"
        self.label_promedio_11 = QLabel(f"Promedio de 11ce : {self.prom_11}")

        self.prom_total = "N/A"
        self.label_promedio_total = QLabel(f"Promedio de todos los estudiantes : {self.prom_total}")


        qvbox.addLayout(form)
        qvbox.addLayout(qhbox_spin)
        qvbox.addWidget(self.combo)
        qvbox.addWidget(self.button_registrar)
        qvbox.addWidget(self.button_borrar)
        qvbox.addWidget(self.label_promedio_9)
        qvbox.addWidget(self.label_promedio_10)
        qvbox.addWidget(self.label_promedio_11)
        qvbox.addWidget(self.label_promedio_total)

        self.frame_izq.setLayout(qvbox)

    def frame_derecho(self):
        qvbox = QVBoxLayout()

        label_español = QLabel("Nota Español")
        self.spin_español = QDoubleSpinBox()
        self.spin_español.setRange(0,5)

        label_matematicas = QLabel("Nota Matematicas")
        self.spin_matematicas = QDoubleSpinBox()
        self.spin_matematicas.setRange(0,5)

        label_fisica = QLabel("Nota Fisica")
        self.spin_fisica = QDoubleSpinBox()
        self.spin_fisica.setRange(0,5)

        label_quimica = QLabel("Nota Quimica")
        self.spin_quimica = QDoubleSpinBox()
        self.spin_quimica.setRange(0,5)


        qvbox.addWidget(label_español)
        qvbox.addWidget(self.spin_español)
        qvbox.addWidget(label_matematicas)
        qvbox.addWidget(self.spin_matematicas)
        qvbox.addWidget(label_fisica)
        qvbox.addWidget(self.spin_fisica)
        qvbox.addWidget(label_quimica)
        qvbox.addWidget(self.spin_quimica)



        self.frame_der.setLayout(qvbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = calculoProm()
    ventana.show()
    sys.exit(app.exec())