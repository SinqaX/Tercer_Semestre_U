from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import sys

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Editor de imágenes simple')
        self.setGeometry(100, 100, 800, 700)

        self.directorio_base = (os.path.dirname(__file__))

        # Cargar imagen
        self.etiqueta_imagen = QLabel(self)
        self.pixmap = QPixmap(os.path.join(self.directorio_base, "img_ejercicios", "forest.png"))
        self.etiqueta_imagen.setPixmap(self.pixmap)
        self.etiqueta_imagen.setFixedSize(600,400)
        self.etiqueta_imagen.setAlignment(Qt.AlignCenter)

        # Crear diales para control RGB
        self.dial_rojo = QDial()
        self.dial_verde = QDial()
        self.dial_azul = QDial()
        
        self.dial_rojo.setRange(0, 255)
        self.dial_verde.setRange(0, 255)
        self.dial_azul.setRange(0, 255)

        self.dial_rojo.valueChanged.connect(self.actualizar_imagen)
        self.dial_verde.valueChanged.connect(self.actualizar_imagen)
        self.dial_azul.valueChanged.connect(self.actualizar_imagen)

        # Crear campos de texto para control RGB
        self.edit_rojo = QLineEdit()
        self.edit_verde = QLineEdit()
        self.edit_azul = QLineEdit()

        self.edit_rojo.returnPressed.connect(lambda: self.actualizar_dial_desde_edit(self.edit_rojo, self.dial_rojo))
        self.edit_verde.returnPressed.connect(lambda: self.actualizar_dial_desde_edit(self.edit_verde, self.dial_verde))
        self.edit_azul.returnPressed.connect(lambda: self.actualizar_dial_desde_edit(self.edit_azul, self.dial_azul))

        # Crear deslizador para control de zoom
        self.deslizador_zoom = QSlider(Qt.Vertical)
        self.deslizador_zoom.setRange(1, 100)
        self.deslizador_zoom.setValue(50)
        self.deslizador_zoom.valueChanged.connect(self.actualizar_zoom)

        img_slider = QHBoxLayout()
        img_slider.addWidget(self.etiqueta_imagen)
        img_slider.addWidget(self.deslizador_zoom)

        # Layouts
        dial_layout = QHBoxLayout()
        dial_layout.addWidget(self.dial_rojo)
        dial_layout.addWidget(self.dial_verde)
        dial_layout.addWidget(self.dial_azul)

        edit_layout = QHBoxLayout()
        edit_layout.addWidget(self.edit_rojo)
        edit_layout.addWidget(self.edit_verde)
        edit_layout.addWidget(self.edit_azul)

        main_layout = QVBoxLayout()
        main_layout.addLayout(img_slider)
        main_layout.addLayout(dial_layout)
        main_layout.addLayout(edit_layout)
        
        self.setLayout(main_layout)

    def actualizar_imagen(self):
        rojo = self.dial_rojo.value()
        verde = self.dial_verde.value()
        azul = self.dial_azul.value()

        self.edit_rojo.setText(str(rojo))
        self.edit_verde.setText(str(verde))
        self.edit_azul.setText(str(azul))

        estilo_fondo = f"background-color: rgb({rojo}, {verde}, {azul});"
        self.etiqueta_imagen.setStyleSheet(estilo_fondo)

    def actualizar_dial_desde_edit(self, edit, dial):

        value = edit.text().strip()
        if value:
            if 0 <= int(value) <= 255:
                dial.setValue(int(value)) 
            else:
                QMessageBox.warning(self, 'Entrada inválida', 'Por favor ingresa un número entre 0 y 255')
        else:
            QMessageBox.warning(self, 'Entrada inválida', 'Por favor no lo dejes vacio')
        


    def actualizar_zoom(self):
        value = self.deslizador_zoom.value() / 50.0
        new_size = self.pixmap.size() * value 
        scaled_pixmap = self.pixmap.scaled(new_size)
        self.etiqueta_imagen.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
