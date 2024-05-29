# #ventanita donde se desplegan varias opciones
#     #qcombobox       .additems("one,", "two")
# #señales
#     #currentindexchanged.connect    proporciona el index
#     #currenttexcahnged   proporciona el texto 


from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

# class Main(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Nombre app")
        
#         # Crear un widget central
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
        
#         # Crear un layout y asignarlo al widget central
#         qvbox = QVBoxLayout(central_widget)
        
#         # Crear el QComboBox y añadir elementos
#         combo = QComboBox()
#         combo.addItems(["one", "two", "three"])
        
#         # Conectar señales a los métodos
#         combo.currentIndexChanged.connect(self.index_changed)
#         combo.currentTextChanged.connect(self.text_changed)
        
#         # Añadir el QComboBox al layout
#         qvbox.addWidget(combo)

#         #editar las opciones de el combobox
#         combo.setEditable(True)

#     def index_changed(self, index):
#         print(f"Current index: {index}")

#     def text_changed(self, text):
#         print(f"Current text: {text}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Main()
#     window.show()
#     sys.exit(app.exec())

#qlistwidget  --

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Equipo de Fútbol")

        qvbox = QVBoxLayout(self)

        label = QLabel("EQUIPO DE FUTBOL", self)
        self.combo = QComboBox(self)
        self.combo.addItems(["Equipo A", "Equipo B", "Equipo C"])
        self.equipos ={"Equipo A":[], "Equipo B":[], "Equipo C":[]}
        self.jugadores = QLineEdit(self)
        self.button_ag_jugador = QPushButton("Agregar Jugador", self)
        self.lista = QListWidget(self)
        self.button_borrar_Equipo = QPushButton("Borrar Equipo", self)
        self.button_borrar_jugador = QPushButton("Borrar Jugador", self)
        self.label_dinamico =QLabel()

        qvbox.addWidget(label)
        qvbox.addWidget(self.combo)
        qvbox.addWidget(self.jugadores)
        qvbox.addWidget(self.button_ag_jugador)
        qvbox.addWidget(self.lista)
        qvbox.addWidget(self.button_borrar_Equipo)
        qvbox.addWidget(self.button_borrar_jugador)
        qvbox.addWidget(self.label_dinamico)

        self.setLayout(qvbox)

        self.button_ag_jugador.clicked.connect(self.agregar_jugador)
        self.button_borrar_Equipo.clicked.connect(self.borrar_equipo)
        self.button_borrar_jugador.clicked.connect(self.borrar_jugador)

        self.combo.currentIndexChanged.connect(self.cambiar_equipo)

    def agregar_jugador(self):
        equipo = self.combo.currentText()
        jugador_ingreso = self.jugadores.text()
        jugador = self.jugadores.text().strip()

        if equipo and jugador:
            if jugador not in self.equipos[equipo]:
                self.equipos[equipo].append(jugador)
                self.jugadores.clear()
                self.lista.addItem(jugador_ingreso)
                self.label_dinamico.setText("")
            else:
                self.label_dinamico.setText("el jugador que intestas agregar ya se encuentra en la lista ")
        else:
            self.label_dinamico.setText("debes proporcionar un jugador para poder agregarlo")

    def borrar_equipo(self):
        equipo_borrar = self.combo.currentText()
        index = self.combo.currentIndex()
        del self.equipos[equipo_borrar]
        self.lista.clear()
        self.label_dinamico.setText(f"el {equipo_borrar} ha sido borrado con exito")
        self.combo.removeItem(index)
        
    def borrar_jugador(self):
        jugador_a_borrar = self.lista.currentItem()
        equipo = self.combo.currentText()
        if jugador_a_borrar:
            jug = jugador_a_borrar.text()
            self.equipos[equipo].remove(jug)
            self.lista.takeItem(self.lista.row(jugador_a_borrar))#borra un elemento especifico de la lista teniendo el indice
        else:
            self.label_dinamico.setText("debe seleccionar un jugador ")

    def cambiar_equipo(self):
        equipo = self.combo.currentText()
        self.lista.clear()
        if equipo in self.equipos:
            jugadores = self.equipos[equipo]
            self.lista.addItems(jugadores)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())