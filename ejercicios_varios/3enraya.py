from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        
        # Directorio base para cargar imágenes
        self.basedir = os.path.dirname(__file__)
        
        # Configuración de la ventana principal
        self.setWindowTitle("App Juego 3 en Raya")
        self.setMinimumSize(450, 600)

        # Layout para manejar las diferentes ventanas
        self.ventanas = QStackedLayout()

        # Diccionario para almacenar los nombres de los jugadores
        self.player_symbols = {"X": "", "O": ""}
        
        # Símbolo del jugador actual (X o O)
        self.current_player = "X"
        
        # Campos de entrada para los nombres de los jugadores
        self.player_x = QLineEdit()
        self.player_o = QLineEdit()
        
        # Estado inicial del juego
        self.game_state = [["" for _ in range(3)] for _ in range(3)]  

        # Configurar las ventanas principales
        self.setup_principal()
        self.setup_juego()
        self.setup_creditos()

        # Establecer el diseño principal de la ventana
        self.setLayout(self.ventanas)
    
    # Configurar la ventana principal
    def setup_principal(self):
        widgetPrincipal = QWidget()
        qvbox = QVBoxLayout()

        # Imagen de título
        labelImg = QLabel()
        img = QPixmap(os.path.join(self.basedir, "img","3enraya","tic_tac_toe.png"))
        labelImg.setPixmap(img.scaled(100,100))
        labelImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Texto de título
        labelText = QLabel("Tres en Raya", self)
        font = labelText.font()
        font.setPointSize(15)
        font.setBold(True)
        labelText.setFont(font)
        labelText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Formulario para ingresar nombres de jugadores
        form = QFormLayout()
        form.addRow("Jugador X", self.player_x)
        form.addRow("Jugador O", self.player_o)

        # Botón para comenzar el juego
        button = QPushButton("Jugar", self)
        button.clicked.connect(self.on_jugar_clicked)

        # Añadir widgets al layout vertical
        qvbox.addWidget(labelImg)
        qvbox.addWidget(labelText)
        qvbox.addLayout(form)
        qvbox.addSpacing(140)
        qvbox.addWidget(button)

        widgetPrincipal.setLayout(qvbox)
        self.ventanas.addWidget(widgetPrincipal)

    # Configurar la ventana del juego
    def setup_juego(self):
        widgetJuego = QWidget()
        qvbox = QVBoxLayout()

        # Etiqueta de título
        labelEstatico = QLabel("TRES EN RAYA", self)
        font = labelEstatico.font()
        font.setPointSize(12)
        font.setBold(True)
        labelEstatico.setFont(font)
        labelEstatico.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta dinámica para mostrar el turno actual
        self.labelDinamico = QLabel("----------", self)
        font = self.labelDinamico.font()
        font.setPointSize(12)
        self.labelDinamico.setFont(font)
        self.labelDinamico.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Cuadrícula para los botones del juego
        qgridbox = QGridLayout()
        qgridbox.setContentsMargins(0,50,0,0)
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton(self)
                button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
                button.setFixedSize(150, 130)
                button.clicked.connect(lambda r=i, c=j: self.on_button_clicked(r, c))
                self.buttons.append(button)
                qgridbox.addWidget(button, i, j)

        # Botón para mostrar los créditos
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        button = QPushButton(self)
        icon = QIcon(os.path.join(self.basedir, "img", "3enraya", "about.png"))
        button.setIcon(icon)
        button.setMaximumSize(button.iconSize())
        button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        button.clicked.connect(lambda: self.ventanas.setCurrentIndex(2))
        hbox.addWidget(button)

        # Añadir widgets al layout vertical
        qvbox.addSpacing(50)
        qvbox.addWidget(labelEstatico)
        qvbox.addWidget(self.labelDinamico)
        qvbox.addLayout(qgridbox)
        qvbox.addLayout(hbox)

        widgetJuego.setLayout(qvbox)
        self.ventanas.addWidget(widgetJuego)

    # Configurar la ventana de créditos
    def setup_creditos(self):
        widgetCreditos = QWidget()
        qvbox = QVBoxLayout()

        # Imagen para los créditos
        labelImg = QLabel()
        img = QPixmap(os.path.join(self.basedir, "img", "3enraya", "tic_tac_toe.png"))
        labelImg.setPixmap(img.scaled(150, 150))
        labelImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Texto de créditos
        labelText = QLabel("by\nSebastian Ordoñez", self)
        font = labelText.font()
        font.setPointSize(13)
        labelText.setFont(font)
        labelText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Botón para regresar al juego
        button = QPushButton(self)
        icon = QIcon(os.path.join(self.basedir, "img", "3enraya", "back_game.png"))
        button.setIcon(icon)
        button.setMaximumSize(button.iconSize())
        button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        button.clicked.connect(lambda: self.ventanas.setCurrentIndex(1))

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)
        hbox.setContentsMargins(0,250,0,0)

        # Añadir widgets al layout vertical
        qvbox.addSpacing(100)
        qvbox.addWidget(labelImg)
        qvbox.addSpacing(0)
        qvbox.addWidget(labelText)
        qvbox.addLayout(hbox)

        widgetCreditos.setLayout(qvbox)
        self.ventanas.addWidget(widgetCreditos)

    # Función para manejar el evento de clic en el botón "Jugar"
    def on_jugar_clicked(self):
        # Obtener los nombres ingresados para los jugadores
        self.player_x_name = self.player_x.text()
        self.player_o_name = self.player_o.text()

        # Verificar si se ingresaron nombres para ambos jugadores
        if self.player_x_name and self.player_o_name:
            # Cambiar a la ventana del juego
            self.ventanas.setCurrentIndex(1)
            # Mostrar el turno del primer jugador
            self.labelDinamico.setText(f"Turno de {self.player_x_name}")
            # Asignar los nombres a los símbolos de los jugadores
            self.player_symbols["X"] = self.player_x_name
            self.player_symbols["O"] = self.player_o_name
        else:
            # Mostrar un mensaje de error si falta algún nombre
            QMessageBox.warning(self, "Error", "Por favor ingresa nombres para ambos jugadores.")
            # Regresar a la ventana principal para ingresar nombres nuevamente
            self.ventanas.setCurrentIndex(0)

    # Función para verificar si el juego ha terminado
    def check_game_over(self):
        # Verificar filas, columnas y diagonales para encontrar un ganador
        for i in range(3):
            # Verificar si hay un ganador en las filas
            if (self.game_state[i][0] == self.game_state[i][1] == self.game_state[i][2] != "" or
                # Verificar si hay un ganador en las columnas
                self.game_state[0][i] == self.game_state[1][i] == self.game_state[2][i] != ""):
                # Obtener el símbolo del ganador
                winning_symbol = self.game_state[i][0] if self.game_state[i][0] == self.game_state[i][1] == self.game_state[i][2] != "" else self.game_state[0][i]
                # Obtener el nombre del jugador correspondiente al símbolo ganador
                winner = self.player_symbols.get(winning_symbol, "")
                # Mostrar el mensaje indicando el ganador
                self.labelDinamico.setText(f"Ha ganado {winner}")
                return True

        # Verificar diagonales
        if (self.game_state[0][0] == self.game_state[1][1] == self.game_state[2][2] != "" or
            self.game_state[0][2] == self.game_state[1][1] == self.game_state[2][0] != ""):
            # Obtener el símbolo del ganador
            winning_symbol = self.game_state[1][1]
            # Obtener el nombre del jugador correspondiente al símbolo ganador
            winner = self.player_symbols.get(winning_symbol, "")
            # Mostrar el mensaje indicando el ganador
            self.labelDinamico.setText(f"Ha ganado {winner}")
            return True

        # Verificar si todas las celdas están llenas (empate)
        all_cells_filled = all(self.game_state[i][j] for i in range(3) for j in range(3))
        if all_cells_filled:
            # Mostrar mensaje de juego terminado en caso de empate
            self.labelDinamico.setText("Juego terminado - Empate")
            return True

        return False



    # Función para manejar el evento de clic en los botones del juego
    def on_button_clicked(self, row, col):
        # Obtener el botón que se ha presionado según la fila y columna
        button = self.buttons[row * 3 + col]
        # Verificar si el botón está vacío y el juego no ha terminado
        if button.text() == "" and not self.check_game_over():
            # Establecer el símbolo del jugador actual en el botón
            button.setText(self.current_player)
            # Actualizar el estado del juego con el símbolo del jugador actual en la posición correspondiente
            self.game_state[row][col] = self.current_player
            # Verificar si el juego ha terminado después de que se hizo un movimiento
            if self.check_game_over():
                # Si el juego ha terminado, salir de la función
                return
            # Cambiar al siguiente jugador para el próximo turno
            self.current_player = "O" if self.current_player == "X" else "X"
            # Obtener el nombre del jugador actual
            player = self.player_symbols.get(self.current_player, "")
            # Actualizar la etiqueta dinámica para mostrar el turno del siguiente jugador
            self.labelDinamico.setText(f"Turno de {player}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
