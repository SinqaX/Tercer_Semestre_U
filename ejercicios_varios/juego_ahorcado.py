from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from random import choice
import os
import sys    

# Lista de palabras para el juego del ahorcado
letras = ["RESPETO","COLOMBIA","TERESA","PASTO","CARRO","ARROZCONPOLLO","CAFECONPAN","PAPITASFRITAS"]

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Juego Del Ahorcado")
        
        # Directorio base para las imágenes
        self.basedir = os.path.dirname(__file__)

        # Crear los layouts principales
        self.layout_padre = QGridLayout()
        self.layout_ahoracado = QHBoxLayout()
        self.layout_letras = QHBoxLayout()
        self.layout_funciones = QVBoxLayout()

        # Establecer márgenes para el layout de funciones
        self.layout_funciones.setContentsMargins(0, 0, 0, 0)

        # Agregar los layouts al layout principal
        self.layout_padre.addLayout(self.layout_ahoracado, 0, 0)
        self.layout_padre.addLayout(self.layout_letras, 0, 1, 2, 1)
        self.layout_padre.addLayout(self.layout_funciones, 1, 1)
        
        self.setLayout(self.layout_padre)

        # Configurar los elementos de la ventana
        self.layoutAhorcado()
        self.layoutletras()
        self.layoutFunciones()



        # Inicializar contador de errores
        self.num_errores = 0

    # def calcularTamañoVentana(self):
    #     # Calcular el tamaño mínimo basado en la longitud de la palabra más larga
    #     longitud_palabra_mas_larga = max(len(word) for word in letras)
    #     ancho_palabra = 30 * longitud_palabra_mas_larga
    #     alto_palabra = 50
    #     ancho_minimo = ancho_palabra + 200
    #     alto_minimo = alto_palabra + 200
    #     self.setMinimumSize(ancho_minimo, alto_minimo)
        
    def layoutAhorcado(self):
        # Crear un contenedor para la imagen del ahorcado
        ahorcado_container = QWidget()
        self.layout_ahoracado.addWidget(ahorcado_container)

        # Crear la etiqueta para la imagen y establecer la imagen inicial
        self.label_imagen = QLabel()
        imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_inicio.png"))
        self.label_imagen.setPixmap(imagen.scaled(200, 200))
        self.label_imagen.setAlignment(Qt.AlignCenter)  
        
        # Agregar la etiqueta al contenedor
        ahorcado_container.setLayout(QHBoxLayout())
        ahorcado_container.layout().addWidget(self.label_imagen)

    def layoutletras(self):
        # Seleccionar una palabra aleatoria
        self.palabra = choice(letras)
        longitud_palabra = len(self.palabra)

        # Crear una lista de letras para la palabra
        self.letras_reveladas = ['_' for _ in range(longitud_palabra)]

        # Crear una etiqueta para mostrar la palabra oculta
        self.label_palabra = QLabel(' '.join(self.letras_reveladas))
        font = QFont("Consolas")
        font.setStyleHint(QFont.TypeWriter)
        font.setPointSize(30)
        self.label_palabra.setFont(font)
        self.layout_letras.addWidget(self.label_palabra)

    def layoutFunciones(self):
        # Crear el layout de la sección de funciones
        funciones = QGridLayout()

        # Crear la etiqueta y el campo de texto para ingresar letras
        label = QLabel("Ingrese Letra")
        self.texto = QLineEdit()
        self.texto.setMaxLength(1)
        self.texto.setFixedSize(30,30)

        # Conectar la señal returnPressed del QLineEdit a la función correspondiente
        self.texto.returnPressed.connect(self.verificarLetra)

        # Aceptar solo letras en el QLineEdit
        self.texto.setValidator(QRegularExpressionValidator(QRegularExpression("[A-Za-z]"), self))

        # Crear el botón para obtener una nueva palabra
        button = QPushButton("Nueva palabra")
        button.clicked.connect(self.actualizarPalabra)
        button.setFixedSize(150,30)

        # Agregar los elementos al layout de funciones
        funciones.addWidget(label, 0, 0, alignment=Qt.AlignLeft)
        funciones.addWidget(self.texto, 0, 0, alignment=Qt.AlignRight)
        funciones.addWidget(button, 1, 0, 1, 2)

        # Agregar el layout de funciones al layout principal
        self.layout_funciones.addLayout(funciones)

        # Crear una etiqueta para mostrar el estado del juego (Game Over o Felicidades)
        self.label_estado = QLabel()
        self.label_estado.setAlignment(Qt.AlignCenter)
        self.layout_padre.addWidget(self.label_estado, 1, 1, 2, 2, alignment=Qt.AlignRight)

    def verificarLetra(self):
        # Obtener la letra ingresada
        letra = self.texto.text().upper()

        # Verificar si la letra está en la palabra
        if letra in self.palabra:
            # Actualizar la palabra oculta con la letra revelada
            for i, letra_palabra in enumerate(self.palabra):
                if letra_palabra == letra:
                    self.letras_reveladas[i] = letra

            # Actualizar la etiqueta con la palabra oculta
            self.label_palabra.setText(' '.join(self.letras_reveladas))

            # Verificar si todas las letras han sido reveladas
            if '_' not in self.letras_reveladas:
                self.label_estado.setText("¡Felicidades! \nHas adivinado la palabra correctamente.")
                self.texto.setDisabled(True)
        else:
            # Incrementar el contador de errores
            self.num_errores += 1

            # Actualizar la imagen del ahorcado
            if self.num_errores == 1:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_1.png"))
            elif self.num_errores == 2:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_2.png"))
            elif self.num_errores == 3:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_3.png"))
            elif self.num_errores == 4:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_4.png"))
            elif self.num_errores == 5:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_5.png"))
            elif self.num_errores == 6:
                imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_final.png"))
            
            self.label_imagen.setPixmap(imagen.scaled(200, 200))

            # Verificar si se alcanzó el máximo de errores (6)
            if self.num_errores == 6:
                # Mostrar "Game Over" y desactivar el QLineEdit
                self.label_estado.setText(f"¡Game Over! \nLa palabra era: {self.palabra}")
                self.texto.setDisabled(True)

    def actualizarPalabra(self):
        # Obtener una nueva palabra aleatoria
        self.palabra = choice(letras)
        longitud_palabra = len(self.palabra)

        # Crear una lista de letras para la palabra
        self.letras_reveladas = ['_' for _ in range(longitud_palabra)]

        # Actualizar la etiqueta con la nueva palabra oculta
        self.label_palabra.setText(' '.join(self.letras_reveladas))

        # Reiniciar el contador de errores
        self.num_errores = 0

        # Reiniciar la imagen del ahorcado
        imagen = QPixmap(os.path.join(self.basedir, "img", "ahorcado_inicio.png"))
        self.label_imagen.setPixmap(imagen.scaled(200, 200))

        # Limpiar la etiqueta de estado del juego
        self.label_estado.clear()
        self.texto.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
