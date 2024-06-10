from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QLabel, QLineEdit, QMessageBox, QCheckBox)
from PySide6.QtGui import QFont, QPixmap
from registro import RegistrarUsuarioView
from main import MainWindow
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
        login_button.clicked.connect(self.login_mainview)

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

    def login_mainview(self):
        users = []
        user_path = "C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Tercer_Semestre_U\\usuarios.txt"

        try:

            with open(user_path, 'r') as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_information = f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in users:
                QMessageBox.information(self,"Inicio De Sesion",
                "Inicio de sesion exitoso!",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()
            else:
                QMessageBox.warning(self, "Error Message",
                "Credenciales incorrectas",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.warning(self, "Error Message",
            f"Base de datos de usuario no encontrada {e}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self, "Error Message",
            f"Error en el servidor {e}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

    def register_user(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()

    def open_main_window(self):
        self.main_window = MainWindow()
        
        self.main_window.show()
        




        

if __name__=="__main__":
    App = QApplication(sys.argv)
    login = Login()
    sys.exit(App.exec())




