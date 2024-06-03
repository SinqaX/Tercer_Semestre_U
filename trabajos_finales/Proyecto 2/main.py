from reproductor_de_musica_ui_ui import Ui_MainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
import pygame

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


class MainMusicApp(QMainWindow, Ui_MainWindow):
    basedir = os.path.dirname(__file__)
    modo_oscuro_activado = False
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pu♩se Music")
        self.setWindowIcon(QIcon(os.path.join(self.basedir, "icons/icons8-music-100.png")))

        self.lista_reproducidas = []  # Lista de canciones reproducidas
        self.indice_actual = 0
        self.paused = False

        self.lista_de_reproduccion = [
        os.path.join(self.basedir, "canciones/Cual es esa, Feid Pirlo.mp3"),
        os.path.join(self.basedir, "canciones/Ey Chory, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Mionca, Maluma Pirlo.mp3"),
        os.path.join(self.basedir, "canciones/LUNA, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Nadie Como Tu, Wisin & Yandel.mp3"),
        os.path.join(self.basedir, "canciones/Normal, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Ojitos Chiquitos, Don Omar.mp3"),
        os.path.join(self.basedir, "canciones/Pa que la pases bien, Arcangel.mp3"),
        os.path.join(self.basedir, "canciones/Remix Exclusivo, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Si sabe Ferxxo, Blessd Feid.mp3"),
        ]

        # Conectar botones stacked
        self.settings_button.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_home_settings.clicked.connect(self.mostrar_pagina_principal)
        self.boton_abrir_perfil_page.clicked.connect(self.mostrar_pagina_perfil)
        self.back_to_home_profile.clicked.connect(self.mostrar_pagina_principal)
        self.ecualizador_button.clicked.connect(self.mostrar_pagina_ecualizador)
        self.about_us_button.clicked.connect(self.mostrar_pagina_about_us)
        self.support_button.clicked.connect(self.mostrar_pagina_soporte)
        self.back_to_config_about.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_equalizer.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_support.clicked.connect(self.mostrar_pagina_settings)
        self.all_songs_button.clicked.connect(self.mostrar_all_songs)
        self.favorite_songs_button.clicked.connect(self.mostrar_favoritas)

        self.mostrar_pagina_principal()
        self.cargar_canciones_iniciales()

        #conexiones ventana principal
        self.cargar_canciones_button.clicked.connect(lambda: self.agregar_archivos(self.lista_de_reproduccion, self.all_songs_list))
        self.pause_button.setCheckable(True)
        self.pause_button.toggled.connect(self.button_toggled)

        pygame.mixer.init()
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_slider)

        # self.pause_button.pressed.connect(lambda : self.reproducir_musica( self.lista_de_reproduccion, self.all_songs_list))
        # self.pause_button.released.connect(self.pausar_musica)

    
    def button_toggled(self, checked):
        if checked:
            self.reproducir_musica(self.lista_de_reproduccion, self.all_songs_list)
        else:
            self.pausar_musica()

    def reproducir_musica(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            # Detener la música actual si está reproduciéndose
            if mixer.music.get_busy():
                mixer.music.stop()

            # Obtener la canción seleccionada
            self.indice_actual = self.seleccionar_cancion(lista_widget)
            if self.indice_actual is not None:
                ruta_archivo, nombre_cancion, duracion_total = lista_de_reproduccion[self.indice_actual]

                # Cargar y reproducir la nueva canción seleccionada
                mixer.music.load(ruta_archivo)
                mixer.music.play()
                self.slider_song.setRange(0, int(duracion_total))
                self.label_12.setText(f"{self.formato_tiempo(duracion_total)}")
                self.paused = False
                self.timer.start(1000)
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
                self.pause_button.setIcon(icon)
                self.lista_reproducidas.append((ruta_archivo, nombre_cancion, duracion_total))


    def pausar_musica(self, mixer=pygame.mixer):
        if self.paused:
            mixer.music.unpause()
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
            self.pause_button.setIcon(icon)
            self.paused = False
        else:
            mixer.music.pause()
            self.paused = True
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
            self.pause_button.setIcon(icon)

    def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            posicion_actual = pygame.mixer.music.get_pos() / 1000
            self.slider_song.setValue(int(posicion_actual))  # Convertir a milisegundos
            self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")
        else:
            self.timer.stop()


    def cargar_canciones_iniciales(self):
        # Cargar canciones predefinidas en el QListWidget
        canciones_procesadas = []
        for archivo in self.lista_de_reproduccion:
            duracion = self.obtener_duracion(archivo)
            nombre_cancion = os.path.basename(archivo)
            canciones_procesadas.append((archivo, nombre_cancion, duracion))
            self.all_songs_list.addItem(nombre_cancion)  # Mostrar el nombre de la canción en el QListWidget
        self.lista_de_reproduccion = canciones_procesadas


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
        lista_widget.addItems([os.path.basename(archivo) for archivo in archivos])  # Mostrar el nombre de la canción en el QListWidget
        self.progress_dialog.close()

    def detener_musica(self, mixer=pygame.mixer, timer=None):
        mixer.music.stop()
        if timer:
            timer.stop()

    def seleccionar_cancion(self, lista_widget, message_box=QMessageBox,mixer=pygame.mixer):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            indice_seleccionado = lista_widget.row(item_seleccionado)
            self.indice_actual = indice_seleccionado
            return indice_seleccionado

        else:
            message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")
            return None

    def formato_tiempo(self, segundos):
        segundos = float(segundos)  # Convertir a flotante si es una cadena de texto
        minutos = int(segundos // 60)
        segundos = int(segundos % 60)
        return f"{minutos:02}:{segundos:02}"
    
    def obtener_duracion(self, ruta_archivo):
        sound = pygame.mixer.Sound(ruta_archivo)
        duracion = sound.get_length()
        return duracion

    def mostrar_dialogo_advertencia(self, message_box=QMessageBox):
        message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")

    def mostrar_pagina_settings(self):
        self.stackedWidget.setCurrentWidget(self.setting_page)

    def mostrar_pagina_principal(self):
        self.stackedWidget.setCurrentWidget(self.principal_page)

    def mostrar_pagina_perfil(self):
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def mostrar_pagina_about_us(self):
        self.stackedWidget.setCurrentWidget(self.about_us_page)

    def mostrar_pagina_ecualizador(self):
        self.stackedWidget.setCurrentWidget(self.equalizer_page)
    
    def mostrar_pagina_soporte(self):
        self.stackedWidget.setCurrentWidget(self.support_page)

    def mostrar_all_songs(self):
        self.stacked_songs.setCurrentWidget(self.all_songs_stack)
    
    def mostrar_favoritas(self):
        self.stacked_songs.setCurrentWidget(self.favorite_songs_stack)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    pygame.mixer.init()  # Inicializar pygame.mixer
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())
