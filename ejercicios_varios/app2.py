# from PySide6.QtWidgets import *
# from PySide6.QtCore import *
# from __feature__ import snake_case, true_property

# import sys

# class MyFirstWindow(QMainWindow):
#     colores = {
#         "gris_suave": (213,211,221),
#         "beige": (239,208,199),
#         "negro": (0,0,0)
#     }
#     def setup_ui(self):
#         self.set_fixed_size(800, 800)

#         #Contenedor del titulo
#         self.fr_titulo = QFrame(self)
#         self.fr_titulo.geometry = QRect(20, 20, 760, 100)
#         self.fr_titulo.style_sheet = f"background-color: rgb{self.colores['gris_suave']};"

#         #Texto de titulo
#         self.titulo = QLabel(self.fr_titulo)
#         self.titulo.text = "Aestethically"
#         self.titulo.geometry = QRect(0, 0, 760, 100)
#         self.titulo.alignment = Qt.AlignCenter
#         self.titulo.style_sheet = f"""
#             color: {self.colores['negro']};
#             font-size: 50px;
#             font-weight: bold;
#             """

#         self.cuadro_principal = QFrame(self)
#         self.cuadro_principal.geometry = QRect(20, 140, 500, 640)
#         self.cuadro_principal.style_sheet = f"background-color: rgb{self.colores['beige']};"

#         #Cuadro principal con inicio de sesion
#         self.iniciar_sesion_texto = QLabel(self.cuadro_principal)
#         self.iniciar_sesion_texto.text = "Iniciar sesión"
#         self.iniciar_sesion_texto.geometry = QRect(20, 30, 500, 50)
#         self.iniciar_sesion_texto.alignment = Qt.AlignCenter
#         self.iniciar_sesion_texto.style_sheet = f"""
#             color: {self.colores['negro']};
#             font-size: 25px;
#             font-weight: bold;
#             """


#         self.cuadro_info = QFrame(self)
#         self.cuadro_info.geometry = QRect(540, 140, 240, 640)
#         self.cuadro_info.style_sheet= f"background-color: rgb{self.colores['gris_suave']};"

# #Ejecutar la app
# app = QApplication(sys.argv)

# window = MyFirstWindow()
# window.setup_ui()
# window.show()

# sys.exit(app.exec_())

#------------------------------------------------------------------------------------------------------------------------------

# from PySide6.QtWidgets import *
# import sys

# class PrimeraVentana(QMainWindow):
#     colores = {
#         "gris_suave": (213,211,221),
#         "beige": (239,208,199)
#     }
#     def setupUi(self):
#         self.setFixedSize(800, 800)

#         self.cuadro1 = QFrame(self)
#         self.cuadro1.setGeometry(20, 20, 760, 100)
#         self.cuadro1.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']};")

#         self.cuadro_principal = QFrame(self)
#         self.cuadro_principal.setGeometry(20, 140, 500, 640)
#         self.cuadro_principal.setStyleSheet(f"background-color: rgb{self.colores['beige']}")

#         self.cuadro_info = QFrame(self)
#         self.cuadro_info.setGeometry(540, 140, 240, 640)
#         self.cuadro_info.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']}")

# app = QApplication(sys.argv)

# window = PrimeraVentana()
# window.setupUi()
# window.show()

# sys.exit(app.exec_())

#--------------------------------------------------------------------------------------------------------------------------------

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys
from random import choice

window_titles = ["mi aplicacion", "tu aplicacion", "que demonios", "pedrito que te pasa", "algo salio mal"]

#subclase que qqwidget que se pude personalizar la ventana 
class MainWindow(QWidget):
    
    def __init__(self):

        super().__init__()

        #atributo para colocar titulo
        self.setWindowTitle("aplicacion con boton")

        #cracion del boton
        button = QPushButton("Press Me!", self)
        button2 = QPushButton("hola!")

        #mover boton con coordenadas (xposicion, yposicion, xtamaño, ytamaño)
        button2.setGeometry(100,30,80,23)
        button.setGeometry(300,30,80,23)

        #configuro el padre donde va a estar el boton
        button.setParent(self)
        button2.setParent(self)

        #coloca color a el cuadro del boton
        button.setStyleSheet("background-color: black; color: white;")
        button2.setStyleSheet("background-color: red; color: white;")

        #señales para el boton
        button.clicked.connect(lambda  : self.presionaElBoton(button))
        #Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas 
        #y anónimas (no es necesario proporcionar un nombre para las funciones lambda). Las funciones 
        #Lambda se comportan como funciones normales declaradas con la palabra clave def 
        # # # button2.clicked.connect(lambda: self.presionaElBoton())

        #tambien se puede utilizar pressed and released igual al clicked
        button.pressed.connect(self.boton_pulsado)
        button.released.connect(self.boton_liberado)

        #tipo de boton a boton de tipo apagador presiono un estado vuelvo a presionar otro estado
        # # # button.setCheckable(True)
        #no se le paasa el parametro ya que cheked esta oculto no es necesario
        # # # button.clicked.connect(self.the_button_was_toggle)

        ##tipo de boton a boton de tipo apagador presiono un estado vuelvo a presionar otro estado / forma lambda
        button2.setCheckable(True)
        #con lambda se debe pasar el parametro explicito
        button2.clicked.connect(lambda cheked: print("verificado?", cheked))

    #funcion o ranura para tipo de boton check / cheked parametro oculto 
    def the_button_was_toggle(self, cheked):
        print("verificado?", cheked)    

    #funcion o ranura cambia titulo y nombre del boton
    def presionaElBoton(self, button):
        self.setWindowTitle("nuevo titulo de la ventana")
        button.setText("me has presionado pedrito!")
        # # # button.setGeometry(300,30,150,23)

        #sizehit para el tamaño del texto y width para ancho y height para alto
        # # # button.resize(button.sizeHint().width(), button.sizeHint().height())

        # # # button.adjustSize()

        # # # button.resize(button.sizeHint())
    
    #ranuras para las señales diferente al clicked
    def boton_pulsado(self):
        print("me has presionado pedrito!")
        
    def boton_liberado(self):
        print("me has liberado pedrito!")

        
        

#se crea la aplicacion
app = QApplication(sys.argv)

#se crea la ventana
window = MainWindow()

#se llama a la ventana
window.show()
app.exec()

#cualquier funcion o metodo en una aplicacion se puede usar como una ranura simplemtente conectando la señal a ella
#si la señal envia datos la funcion o ranura debe capturar esos datos 
