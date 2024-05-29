# from PySide6.QtWidgets import *
# from PySide6.QtGui import *
# from PySide6.QtCore import *
# import sys
# import os

# class MainWindows(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Mord")

#         basedir = os.path.dirname(__file__)

#         qprincipal = QVBoxLayout(self)

#         layoutbotones = QHBoxLayout(self)
        

#         buton_negrita = QPushButton("N",self)
#         buton_negrita.adjustSize()

#         button_alinear_derecha = QPushButton(self)
#         icon_alinear_derecha = QIcon(os.path.join(basedir, "img", "img_ejer", "alinear-a-la-derecha.png"))
#         button_alinear_derecha.setIcon(icon_alinear_derecha)
#         button_alinear_derecha.setMaximumSize(button_alinear_derecha.iconSize())
#         button_alinear_derecha.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

#         button_alinear_izquierda = QPushButton(self)
#         icon_alinear_izquierda = QIcon(os.path.join(basedir, "img", "img_ejer", "alinear-a-la-izquierda.png"))
#         button_alinear_izquierda.setIcon(icon_alinear_izquierda)
#         button_alinear_izquierda.setMaximumSize(button_alinear_izquierda.iconSize())
#         button_alinear_izquierda.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        




#         self.editor = QPlainTextEdit(self)

#         form = QFormLayout()





        

#         layoutbotones.addWidget(buton_negrita)
#         layoutbotones.addWidget(button_alinear_derecha)
#         layoutbotones.addWidget(button_alinear_izquierda)
        
#         qprincipal.addLayout(layoutbotones)
#         qprincipal.addWidget(self.editor)
        
        


        


# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindows()
#     window.show()
#     sys.exit(app.exec())


from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import os

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mord")

        basedir = os.path.dirname(__file__)
        print(f"Directorio base: {basedir}")

        layout_principal = QVBoxLayout(self)

        layout_botones = QHBoxLayout()

        # Botón Negrita
        boton_negrita = QPushButton("N", self)
        boton_negrita.clicked.connect(self.negrita)
        boton_negrita.adjustSize()  # Ajusta el tamaño del botón al contenido del texto

        # Botón Alinear a la Derecha
        path_alinear_derecha = os.path.join(basedir, "img", "img_ejer", "alinear-a-la-derecha.png")
        boton_alinear_derecha = QPushButton(self)
        icono_alinear_derecha = QIcon(path_alinear_derecha)
        boton_alinear_derecha.setIcon(icono_alinear_derecha)
        boton_alinear_derecha.setMaximumSize(50, 50)
        boton_alinear_derecha.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        boton_alinear_derecha.adjustSize()
        boton_alinear_derecha.clicked.connect(self.alinear_derecha)

        # Botón Alinear a la Izquierda
        path_alinear_izquierda = os.path.join(basedir, "img", "img_ejer", "alinear-a-la-izquierda.png")
        boton_alinear_izquierda = QPushButton(self)
        icono_alinear_izquierda = QIcon(path_alinear_izquierda)
        boton_alinear_izquierda.setIcon(icono_alinear_izquierda)
        boton_alinear_izquierda.setMaximumSize(50, 50)
        boton_alinear_izquierda.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        boton_alinear_izquierda.adjustSize()
        boton_alinear_izquierda.clicked.connect(self.alinear_izquierda)

        # Botón Alinear al Centro
        path_alinear_centro = os.path.join(basedir, "img", "img_ejer", "alinear.png")
        boton_alinear_centro = QPushButton(self)
        icono_alinear_centro = QIcon(path_alinear_centro)
        boton_alinear_centro.setIcon(icono_alinear_centro)
        boton_alinear_centro.setMaximumSize(50, 50)
        boton_alinear_centro.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        boton_alinear_centro.adjustSize()
        boton_alinear_centro.clicked.connect(self.alinear_centro)

        # Botón Mayúsculas
        path_mayusculas = os.path.join(basedir, "img", "img_ejer", "boton-de-interfaz-en-mayusculas.png")
        boton_mayusculas = QPushButton(self)
        icono_mayusculas = QIcon(path_mayusculas)
        boton_mayusculas.setIcon(icono_mayusculas)
        boton_mayusculas.setMaximumSize(50, 50)
        boton_mayusculas.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        boton_mayusculas.adjustSize()
        boton_mayusculas.clicked.connect(self.convertir_mayusculas)

        # Botón Minúsculas
        path_minusculas = os.path.join(basedir, "img", "img_ejer", "simbolo-de-interfaz-en-minusculas.png")
        boton_minusculas = QPushButton(self)
        icono_minusculas = QIcon(path_minusculas)
        boton_minusculas.setIcon(icono_minusculas)
        boton_minusculas.setMaximumSize(50, 50)
        boton_minusculas.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        boton_minusculas.adjustSize()
        boton_minusculas.clicked.connect(self.convertir_minusculas)

        self.editor = QPlainTextEdit(self)

        layout_botones.addWidget(boton_negrita)
        layout_botones.addWidget(boton_alinear_derecha)
        layout_botones.addWidget(boton_alinear_izquierda)
        layout_botones.addWidget(boton_alinear_centro)
        layout_botones.addWidget(boton_mayusculas)
        layout_botones.addWidget(boton_minusculas)

        layout_principal.addLayout(layout_botones)
        layout_principal.addWidget(self.editor)

    def negrita(self):
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            fmt = cursor.charFormat()
            fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
            cursor.mergeCharFormat(fmt)
        else:
            font = self.editor.font()
            font.setBold(not font.bold())
            self.editor.setFont(font)

    def alinear_derecha(self):
        self.alinear(Qt.AlignRight)

    def alinear_izquierda(self):
        self.alinear(Qt.AlignLeft)

    def alinear_centro(self):
        self.alinear(Qt.AlignCenter)

    def alinear(self, alignment):
        text = self.editor.toPlainText()
        lines = text.split('\n')
        width = self.editor.fontMetrics().horizontalAdvance(max(lines, key=len))
        aligned_text = []

        for line in lines:
            if alignment == Qt.AlignRight:
                aligned_text.append(line.rjust(width))
            elif alignment == Qt.AlignCenter:
                aligned_text.append(line.center(width))
            else:
                aligned_text.append(line.ljust(width))

        self.editor.setPlainText('\n'.join(aligned_text))

    def convertir_mayusculas(self):
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            texto_seleccionado = cursor.selectedText()
            cursor.insertText(texto_seleccionado.upper())
        else:
            self.editor.setPlainText(self.editor.toPlainText().upper())

    def convertir_minusculas(self):
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            texto_seleccionado = cursor.selectedText()
            cursor.insertText(texto_seleccionado.lower())
        else:
            self.editor.setPlainText(self.editor.toPlainText().lower())

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())


