import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class GestorDeTareas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 350, 450)

        # Widget principal
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        # Diseños (Layouts)
        self.diseño_principal = QVBoxLayout()
        self.diseño_botones = QVBoxLayout()
        self.widget_central.setLayout(self.diseño_principal)

        # Lista de tareas
        self.lista_tareas = QListWidget()
        self.lista_tareas.setSelectionMode(QListWidget.MultiSelection)
        self.lista_tareas.itemDoubleClicked.connect(self.editar_tarea)
        self.diseño_principal.addWidget(self.lista_tareas)

        # Botones
        self.boton_agregar_tarea = QPushButton("Agregar Tarea")
        self.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.diseño_botones.addWidget(self.boton_agregar_tarea)

        self.boton_completar_tarea = QPushButton("Marcar como Completada")
        self.boton_completar_tarea.clicked.connect(self.marcar_tarea_completada)
        self.diseño_botones.addWidget(self.boton_completar_tarea)

        self.boton_eliminar_tarea = QPushButton("Eliminar Tarea")
        self.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea)
        self.diseño_botones.addWidget(self.boton_eliminar_tarea)

        self.boton_guardar_lista = QPushButton("Guardar Lista de Tareas")
        self.boton_guardar_lista.clicked.connect(self.guardar_lista_tareas)
        self.diseño_botones.addWidget(self.boton_guardar_lista)

        self.boton_cargar_lista = QPushButton("Cargar Lista de Tareas")
        self.boton_cargar_lista.clicked.connect(self.cargar_lista_tareas)
        self.diseño_botones.addWidget(self.boton_cargar_lista)

        self.label_dinamico = QLabel("")
        self.label_dinamico.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.diseño_botones.addWidget(self.label_dinamico)

        self.diseño_principal.addLayout(self.diseño_botones)

    def agregar_tarea(self):
        tarea, ok = QInputDialog.getText(self, "Agregar Tarea", "Ingrese la nueva tarea:")
        if ok and tarea.strip():
            self.lista_tareas.addItem(tarea)
            self.label_dinamico.setText("La tarea se agregó con éxito")
        else:
            self.label_dinamico.setText("La tarea debe contener texto para ser agregada")

    def editar_tarea(self, item):
        tarea, ok = QInputDialog.getText(self, "Editar Tarea", "Modifique la tarea:", text=item.text())
        if ok and tarea:
            item.setText(tarea)
            self.label_dinamico.setText("La tarea ha sido modificada")

    def marcar_tarea_completada(self):
        for item in self.lista_tareas.selectedItems():
            respuesta = QMessageBox.question(
                self, "Confirmar Completar", "¿Estás seguro de que deseas marcar esta tarea como completada?",
            )
            if respuesta == QMessageBox.Yes:
                item.setCheckState(Qt.Checked)
                self.label_dinamico.setText("La tarea se marcó con éxito")

    def eliminar_tarea(self):
        for item in self.lista_tareas.selectedItems():
            respuesta = QMessageBox.question(
                self, "Confirmar Eliminación", "¿Estás seguro de que deseas eliminar esta tarea?",
            )

            if respuesta == QMessageBox.Yes:
                self.lista_tareas.takeItem(self.lista_tareas.row(item))
                self.label_dinamico.setText("La tarea se eliminó con éxito")

    def guardar_lista_tareas(self):
        opciones = QFileDialog.Options()
        ruta_archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar Lista de Tareas", "", "Text Files (*.txt);;All Files (*)", options=opciones
        )
        if ruta_archivo:
            with open(ruta_archivo, 'w') as archivo:
                for indice in range(self.lista_tareas.count()):
                    item = self.lista_tareas.item(indice)
                    tarea = item.text()
                    completada = item.checkState() == Qt.Checked
                    archivo.write(f"{tarea}|{completada}\n")
        self.label_dinamico.setText("La lista de tareas se guardó con éxito")

    def cargar_lista_tareas(self):
        opciones = QFileDialog.Options()
        ruta_archivo, _ = QFileDialog.getOpenFileName(
            self, "Cargar Lista de Tareas", "", "Text Files (*.txt);;All Files (*)", options=opciones
        )
        if ruta_archivo:
            self.lista_tareas.clear()
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    tarea, completada = linea.strip().split('|')
                    item = QListWidgetItem(tarea)
                    if completada == 'True':
                        item.setCheckState(Qt.Checked)
                    self.lista_tareas.addItem(item)
        self.label_dinamico.setText("La lista de tareas se cargó con éxito")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorDeTareas()
    ventana.show()
    sys.exit(app.exec())
