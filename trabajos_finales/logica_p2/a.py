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
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                self.pause_button.setIcon(icon)
                self.lista_reproducidas.append((ruta_archivo, nombre_cancion, duracion_total))

def pausar_musica(self, mixer=pygame.mixer):
        if self.paused:
            mixer.music.unpause()
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
            self.pause_button.setIcon(icon)
            self.paused = False
        else:
            mixer.music.pause()
            self.paused = True
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
            self.pause_button.setIcon(icon)

def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            posicion_actual = pygame.mixer.music.get_pos() / 1000
            self.slider_song.setValue(int(posicion_actual))  # Convertir a milisegundos
            self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")
        else:
            self.timer.stop()
    
def detener_musica(self, mixer=pygame.mixer, timer=None):
        mixer.music.stop()
        if timer:
            timer.stop()