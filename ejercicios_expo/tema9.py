from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cambios de fuente")

        layout_principal = QHBoxLayout()
        layout_izquierdo = QVBoxLayout()
        layout_derecho = QVBoxLayout()

        self.combo_fuente = QFontComboBox()
        layout_izquierdo.addWidget(self.combo_fuente)

        self.boton_cambiar_fuente = QPushButton("Cambiar fuente")
        self.boton_cambiar_fuente.clicked.connect(self.cambiar_fuente)
        layout_izquierdo.addWidget(self.boton_cambiar_fuente)

        self.cuadro_texto = QTextEdit()
        layout_derecho.addWidget(self.cuadro_texto)

        self.boton_soccer = QPushButton("Soccer League College")
        self.boton_soccer.clicked.connect(lambda: self.establecer_fuente("Soccer League College"))
        layout_izquierdo.addWidget(self.boton_soccer)

        self.boton_bodoni = QPushButton("Bodoni")
        self.boton_bodoni.clicked.connect(lambda: self.establecer_fuente("Bodoni"))
        layout_izquierdo.addWidget(self.boton_bodoni)

        self.boton_rockwell = QPushButton("Rockwell")
        self.boton_rockwell.clicked.connect(lambda: self.establecer_fuente("Rockwell"))
        layout_izquierdo.addWidget(self.boton_rockwell)

        self.boton_dialogo_fuente = QPushButton("Seleccionar fuente")
        self.boton_dialogo_fuente.clicked.connect(self.abrir_dialogo_fuente)
        layout_izquierdo.addWidget(self.boton_dialogo_fuente)

        self.boton_limpiar = QPushButton()
        self.boton_limpiar.clicked.connect(self.cuadro_texto.clear)
        icon = QIcon("C:\\Users\\SEBASTIAN\\OneDrive\\Escritorio\\archivos ejercicios exposicion\\QFontComboBox_QFontDialog\\QFontComboBox_QFontDialog\\limpio.png")
        self.boton_limpiar.setIcon(icon)
        layout_derecho.addWidget(self.boton_limpiar)
        

        layout_principal.addLayout(layout_izquierdo)
        layout_principal.addLayout(layout_derecho)

        self.setLayout(layout_principal)

    def cambiar_fuente(self):
        fuente_seleccionada = self.combo_fuente.currentFont()
        self.cuadro_texto.setCurrentFont(fuente_seleccionada)

    def establecer_fuente(self, nombre_fuente):
        fuente = QFont(nombre_fuente, 12)
        self.cuadro_texto.setCurrentFont(fuente)

    def abrir_dialogo_fuente(self):
        ok, fuente_dialogo = QFontDialog.getFont()
        if ok:
            self.cuadro_texto.setCurrentFont(fuente_dialogo)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
