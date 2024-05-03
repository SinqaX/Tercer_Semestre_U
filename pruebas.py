from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import os

from PySide6.QtWidgets import QWidget

# class mainWindow(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.ventanas = QStackedLayout()

#         self.setWindowTitle("tres en raya")
#         self.setMinimumSize(450,600)

#         self.basedir = os.path.dirname(__file__)

#         self.primera()
#         self.segunda()
#         self.tercera()


#         self.setLayout(self.ventanas)



#     def primera(self):

#         widget = QWidget()
#         qvbox = QVBoxLayout()

#         label_img = QLabel()
#         img = QPixmap(os.path.join(self.basedir, "img", "3enraya", "tic_tac_toe.png"))
#         label_img.setPixmap(img.scaled(120,120))
#         label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)


#         label = QLabel("Tres En Raya")
#         label.setFont(QFont("Courier", 19))
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         qform = QFormLayout()
#         self.player_x = QLineEdit()
#         self.player_o = QLineEdit()
#         qform.addRow("Jugador X", self.player_x)
#         qform.addRow("Jugador O", self.player_o)


#         button = QPushButton("Jugar", self)
#         button.clicked.connect(lambda: self.ventanas.setCurrentIndex(1))


#         qvbox.addWidget(label_img)
#         qvbox.addWidget(label)
#         qvbox.addLayout(qform) 
#         qvbox.addSpacing(120)
#         qvbox.addWidget(button)


#         widget.setLayout(qvbox)
#         self.ventanas.addWidget(widget)



#     def segunda(self):
#         widget = QWidget()
#         qvbox = QVBoxLayout()


#         label = QLabel("Tres En Raya")
#         label.setFont(QFont("Courier", 15))
#         label.font().setBold(True)
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)


#         self.label_dinamico = QLabel("Turno de ", self)
#         self.label_dinamico.setFont(QFont("Courier", 15))
#         self.label_dinamico.font().setBold(True)
#         self.label_dinamico.setAlignment(Qt.AlignmentFlag.AlignCenter)



#         qgridbox = QGridLayout()
#         for i in range(3):
#             for j in range(3):
#                 button = QPushButton()
#                 button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
#                 button.setFixedSize(130,130)
#                 qgridbox.addWidget(button, i, j)

        
#         button = QPushButton()
#         icon = QIcon(os.path.join(self.basedir, "img", "3enraya", "back_game.png"))
#         button.setIcon(icon)
#         button.setFixedSize(19,15)
#         button.clicked.connect(lambda: self.ventanas.setCurrentIndex(2))


#         qvbox.addWidget(label)
#         qvbox.addWidget(self.label_dinamico)
#         qvbox.addLayout(qgridbox)
#         qvbox.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)



#         widget.setLayout(qvbox)
#         self.ventanas.addWidget(widget)

#     def tercera(self):
        
#         widget = QWidget()
#         qvbox = QVBoxLayout()

#         label_img = QLabel()
#         img = QPixmap(os.path.join(self.basedir, "img", "3enraya", "tic_tac_toe.png"))
#         label_img.setPixmap(img.scaled(110,110))
#         label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)


#         label = QLabel("By\n Sebastian David Ordoñez Bolaños")
#         label.setFont(QFont("Courier", 15))
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         button = QPushButton()
#         icon = QIcon(os.path.join(self.basedir, "img", "3enraya", "about.png"))
#         button.setIcon(icon)
#         button.setFixedSize(19,15)

#         qvbox.addSpacing(100)
#         qvbox.addWidget(label_img)
#         qvbox.setSpacing(0)
#         qvbox.addWidget(label)
#         qvbox.addSpacing(180)
#         qvbox.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
#         button.clicked.connect(lambda: self.ventanas.setCurrentIndex(1))

#         widget.setLayout(qvbox)
#         self.ventanas.addWidget(widget)




# class mainWindow(QWidget):

#     def __init__(self):
#         super().__init__()
#         colores = ["green", "blue", "yellow", "pink", "gray", "orange", "purple"]

#         self.setWindowTitle("Colores")
#         self.setMinimumSize(30
#                              0,180)

#         principal = QHBoxLayout()

#         qvbox1 = QVBoxLayout()
#         qvbox2 = QVBoxLayout()
#         label = QLabel("4")
#         label.setFont(QFont("Courier", 60))
#         label.font().setBold(True)
#         label.setAutoFillBackground(True)
#         pallete = label.palette()
#         pallete.setColor(QPalette.Window, colores[6])
#         label.setPalette(pallete)
#         qvbox2.addWidget(label)
#         qvbox3 = QVBoxLayout()
        
#         for i in range(6):
#             if i<3:
#                 label = QLabel(f"{i+1}")
#                 label.setFont(QFont("Courier", 60))
#                 label.font().setBold(True)
#                 label.setAutoFillBackground(True)
#                 pallete = label.palette()
#                 pallete.setColor(QPalette.Window, colores[i])
#                 label.setPalette(pallete)
#                 qvbox1.addWidget(label)
#             else:
#                 if i == 4:
#                     qvbox3.addSpacing(40)
#                 else:
#                     qvbox3.setSpacing(0)

#                 label = QLabel(f"{i+1}")
#                 label.setFont(QFont("Courier", 60))
#                 label.font().setBold(True)
#                 label.setAutoFillBackground(True)
#                 pallete = label.palette()
#                 pallete.setColor(QPalette.Window, colores[i])
#                 label.setPalette(pallete)
                
#                 qvbox3.addWidget(label)

#         principal.addLayout(qvbox1)
#         principal.addLayout(qvbox2)
#         principal.addLayout(qvbox3)
        
#         self.setLayout(principal)

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()

        qvbox_principal = QVBoxLayout()
        self.check_principal = QCheckBox("Todos")
        self.check_principal.clicked.connect(self.principal)

        group = QGroupBox()
        qvbox = QVBoxLayout()
        qvbox.setSpacing(0)
        self.check_1 = QCheckBox("Amarillo")
        self.check_2 = QCheckBox("Azul")
        self.check_3 = QCheckBox("Rojo")
        self.check_1.clicked.connect(self.secundario)
        self.check_2.clicked.connect(self.secundario)
        self.check_3.clicked.connect(self.secundario)
        qvbox.addWidget(self.check_1)
        qvbox.addWidget(self.check_2)
        qvbox.addWidget(self.check_3)
        group.setLayout(qvbox)

        qvbox_principal.addWidget(self.check_principal)
        qvbox_principal.addWidget(group)
        
        self.setLayout(qvbox_principal)

    def principal(self):    
        self.check_principal.setTristate(False)
        if self.check_principal.isChecked():
            self.check_1.setChecked(True)
            self.check_2.setChecked(True)
            self.check_3.setChecked(True)
        else: 
            self.check_1.setChecked(False)
            self.check_2.setChecked(False)
            self.check_3.setChecked(False)

    def secundario(self):
        self.check_principal.setTristate(True)

        cheked = sum([self.check_1.isChecked(),
                      self.check_2.isChecked(),
                      self.check_3.isChecked()])
        
        if cheked == 3:
            self.check_principal.setCheckState(Qt.Checked)
        elif cheked == 0:
            self.check_principal.setCheckState(Qt.Unchecked)
        else:
            self.check_principal.setCheckState(Qt.PartiallyChecked)
            

        


if __name__=="__main__":
    app = QApplication([])
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
