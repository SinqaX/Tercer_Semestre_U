from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QLabel, QLineEdit, QMessageBox, QCheckBox)
from PySide6.QtGui import QFont, QPixmap
from registro import RegistrarUsuarioView
import sys


class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.start_iu()
    
    def start_iu(self):
        #crea la ventana la llama
        self.setGeometry(100,100, 350, 250)
        self.setWindowTitle("Login App")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        #objeto Qlabel para texto en ventana 
        user_label = QLabel(self)
        user_label.setText("User")
        user_label.setFont(QFont("Arial", 10))
        user_label.move(20,54)

        #objeto QlineEdit para recibir informacion
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)#ancho, alto
        self.user_input.move(90,50)

        #objeto Qlabel para texto en ventana 
        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont("Arial", 10))
        password_label.move(20,86)

        #objeto QlineEdit para recibir informacion
        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)  # width, height
        self.password_input.move(90, 82)
        #metodo que bloquea la visibilidad de los datos ingresados
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        #boton tipo check para activar o desactivar la visibilidad 
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("View Password")
        self.check_view_password.move(90,110)
        self.check_view_password.toggled.connect(self.view_password)

        #boton login
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.iniciar_mainview)

        #boton registrate
        register_button = QPushButton(self)
        register_button.setText("Registrate")
        register_button.resize(320,34)
        register_button.move(20,180)
        register_button.clicked.connect(self.register_user)


    def view_password(self,clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciar_mainview(self):
        pass

    def register_user(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()
        




        

if __name__=="__main__":
    App = QApplication(sys.argv)
    login = Login()
    sys.exit(App.exec())




