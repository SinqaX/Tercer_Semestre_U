import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pygame
import os 

class CargarArchivosThread(QThread):
    progreso = Signal(int)
    archivos_cargados = Signal(list)

    def __init__(self, archivos):
        super().__init__()
        self.archivos = archivos

    def run(self):
        archivos_cargados = []
        total_archivos = len(self.archivos)
        for i, archivo in enumerate(self.archivos):
            archivos_cargados.append(archivo)
            progreso = int((i + 1) / total_archivos * 100)
            self.progreso.emit(progreso)
        self.archivos_cargados.emit(archivos_cargados)

class ReproductorDeMusica(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reproductor de Música")
        self.setGeometry(300, 300, 500, 400)

        self.lista_de_reproduccion = []
        self.lista_reproducidas = []  # Lista de canciones reproducidas
        self.indice_actual = 0
        self.modo_reproduccion = "secuencial"
        self.paused = False

        layout = QVBoxLayout()

        self.boton_abrir = QPushButton("Añadir Canciones")
        self.boton_abrir.clicked.connect(lambda: self.agregar_archivos(self.lista_de_reproduccion, self.lista_widget))
        layout.addWidget(self.boton_abrir)

        self.lista_widget = QListWidget()
        self.lista_widget.itemDoubleClicked.connect(lambda: self.seleccionar_cancion(self.lista_widget))
        layout.addWidget(self.lista_widget)

        control_layout = QHBoxLayout()

        self.boton_reproducir = QPushButton("Reproducir")
        self.boton_reproducir.clicked.connect(lambda: self.reproducir_musica(self.lista_de_reproduccion, self.lista_widget))
        control_layout.addWidget(self.boton_reproducir)

        self.boton_pausa = QPushButton("Pausar")
        self.boton_pausa.clicked.connect(lambda: self.pausar_musica())
        control_layout.addWidget(self.boton_pausa)

        self.boton_siguiente = QPushButton("Siguiente")
        self.boton_siguiente.clicked.connect(lambda: self.siguiente_cancion(self.lista_de_reproduccion, self.lista_widget))
        control_layout.addWidget(self.boton_siguiente)

        self.boton_anterior = QPushButton("Anterior")
        self.boton_anterior.clicked.connect(lambda: self.cancion_anterior(self.lista_de_reproduccion, self.lista_widget))
        control_layout.addWidget(self.boton_anterior)

        self.boton_modo = QPushButton("Modo: Secuencial")
        self.boton_modo.clicked.connect(lambda: self.cambiar_modo(self.boton_modo))
        control_layout.addWidget(self.boton_modo)

        layout.addLayout(control_layout)
        
        self.label_cancion = QLabel("")
        layout.addWidget(self.label_cancion)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.sliderMoved.connect(lambda: self.cambiar_posicion(self.slider, self.lista_de_reproduccion))

        layout.addWidget(self.slider)

        self.label_tiempo = QLabel("00:00 / 00:00")
        layout.addWidget(self.label_tiempo)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        pygame.mixer.init()
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_slider)


    def agregar_archivos(self, lista_de_reproduccion, lista_widget, file_dialog=QFileDialog, progress_dialog_class=QProgressDialog, thread_class=CargarArchivosThread):
        archivos, _ = file_dialog.getOpenFileNames(self, "Abrir Archivos de Música", "", "Archivos de Música (*.mp3 *.wav)")
        if archivos:
            self.progress_dialog = progress_dialog_class("Cargando canciones...", "Cancelar", 0, 100, self)
            self.progress_dialog.setWindowTitle("Progreso")
            self.progress_dialog.setWindowModality(Qt.WindowModal)
            self.progress_dialog.show()

            self.cargar_archivos_thread = thread_class(archivos)
            self.cargar_archivos_thread.progreso.connect(self.progress_dialog.setValue)
            self.cargar_archivos_thread.archivos_cargados.connect(lambda archivos: self.procesar_archivos_cargados(archivos, lista_de_reproduccion, lista_widget))
            self.cargar_archivos_thread.start()

    def procesar_archivos_cargados(self, archivos, lista_de_reproduccion, lista_widget):
        for archivo in archivos:
            duracion = self.obtener_duracion(archivo)
            nombre_cancion = os.path.basename(archivo)  # Obtener solo el nombre del archivo sin la ruta
            lista_de_reproduccion.append((archivo, nombre_cancion, duracion))  # Agregar la duración también
        lista_widget.addItems([archivo[1] for archivo in lista_de_reproduccion])  # Mostrar el nombre de la canción en el QListWidget
        self.progress_dialog.close()


    def mostrar_dialogo_advertencia(self, message_box=QMessageBox):
        message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")


    def detener_musica(self, mixer=pygame.mixer, timer=None):
        mixer.music.stop()
        if timer:
            timer.stop()

    def seleccionar_cancion(self, lista_widget, message_box=QMessageBox):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            indice_seleccionado = lista_widget.row(item_seleccionado)
            self.indice_actual = indice_seleccionado
            return indice_seleccionado
        else:
            message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")
            return None


    def pausar_musica(self, mixer=pygame.mixer):
        if self.paused:
            mixer.music.unpause()
            self.paused = False
        else:
            mixer.music.pause()
            self.paused = True

    def siguiente_cancion(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            print("Modo de reproducción:", self.modo_reproduccion)
            print("Índice actual antes del cambio:", self.indice_actual)
            if self.modo_reproduccion == "secuencial":
                self.indice_actual = (self.indice_actual + 1) % len(lista_de_reproduccion)
            elif self.modo_reproduccion == "aleatorio":
                nuevo_indice = self.indice_actual
                while nuevo_indice == self.indice_actual:
                    nuevo_indice = random.randint(0, len(lista_de_reproduccion) - 1)
                self.indice_actual = nuevo_indice
            elif self.modo_reproduccion == "bucle":
                self.detener_musica(mixer, self.timer)
            lista_widget.setCurrentRow(self.indice_actual)
            print("Índice actual después del cambio:", self.indice_actual)
            self.reproducir_musica(lista_de_reproduccion, lista_widget)

    def cancion_anterior(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            if self.modo_reproduccion == "aleatorio":
                if len(self.lista_reproducidas) <= 1:
                    return
                # Eliminar la canción actual de la lista de reproducidas
                self.lista_reproducidas.pop()
                # Establecer la canción anterior como la actual
                ruta_archivo, nombre_cancion, duracion_total = self.lista_reproducidas[-1]
                self.indice_actual = lista_de_reproduccion.index((ruta_archivo, nombre_cancion, duracion_total))
            else:
                self.indice_actual = (self.indice_actual - 1) % len(lista_de_reproduccion)
            lista_widget.setCurrentRow(self.indice_actual)
            self.reproducir_musica(lista_de_reproduccion, lista_widget)


    def reproducir_musica(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                self.indice_actual = self.seleccionar_cancion(lista_widget)
                if self.indice_actual is not None:
                    ruta_archivo, nombre_cancion, duracion_total = lista_de_reproduccion[self.indice_actual]
                    mixer.music.load(ruta_archivo)
                    mixer.music.play()
                    self.slider.setRange(0, int(duracion_total))
                    self.timer.start(1000)
                    self.paused = False
                    self.label_cancion.setText(nombre_cancion)
                    self.lista_reproducidas.append((ruta_archivo, nombre_cancion, duracion_total))


    def cambiar_modo(self, boton_modo):
        modos = ["secuencial", "aleatorio", "bucle"]
        indice_modo_actual = modos.index(self.modo_reproduccion)
        self.modo_reproduccion = modos[(indice_modo_actual + 1) % len(modos)]
        boton_modo.setText(f"Modo: {self.modo_reproduccion.capitalize()}")

    def cambiar_posicion(self, slider, lista_de_reproduccion, mixer=pygame.mixer):
        if mixer.music.get_busy():
            nueva_posicion = slider.value()
            duracion_total = lista_de_reproduccion[self.indice_actual][2]
            mixer.music.set_pos(nueva_posicion / 1000 * duracion_total)



    def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            posicion_actual = pygame.mixer.music.get_pos() / 1000
            duracion_total = self.lista_de_reproduccion[self.indice_actual][2]  # La duración total está en la posición 2
            self.slider.setValue(int(posicion_actual))  # Convertir a milisegundos
            self.label_tiempo.setText(f"{self.formato_tiempo(posicion_actual)} / {self.formato_tiempo(duracion_total)}")
        else:
            self.timer.stop()


    def obtener_duracion(self, ruta_archivo):
        sound = pygame.mixer.Sound(ruta_archivo)
        duracion = sound.get_length()
        return duracion

    def formato_tiempo(self, segundos):
        segundos = float(segundos)  # Convertir a flotante si es una cadena de texto
        minutos = int(segundos // 60)
        segundos = int(segundos % 60)
        return f"{minutos:02}:{segundos:02}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reproductor = ReproductorDeMusica()
    reproductor.show()
    sys.exit(app.exec())

