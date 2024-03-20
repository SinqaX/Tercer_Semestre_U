from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QLabel, QLineEdit, QMessageBox, QCheckBox)
from PySide6.QtGui import QFont, QPixmap
import sys


class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.start_iu()
    
    def start_iu(self):
        self.setGeometry(100,100, 350, 250)
        self.setWindowTitle("Login App")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("User")
        user_label.setFont(QFont("Arial", 10))
        user_label.move(20,54)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)#ancho, alto
        self.user_input.move(90,50)

        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont("Arial", 10))
        password_label.move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)  # width, height
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("View Password")
        self.check_view_password.move(90,110)
        
        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320,34)
        login_button.move(20,140)

        register_button = QPushButton(self)
        register_button.setText("Registrate")
        register_button.resize(320,34)
        register_button.move(20,180)
        




        

if __name__=="__main__":
    App = QApplication(sys.argv)
    login = Login()
    sys.exit(App.exec())




