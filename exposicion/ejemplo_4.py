
import sys
from PySide6.QtWidgets import QApplication, QProgressDialog, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

class MainProgressDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setWindowTitle('Ejemplo de QProgressDialog')
        self.setGeometry(450, 500, 350, 100)


        #se crea el progressdialog           texto del label, texto del boton, minimum, maximum
        self.progressdialog = QProgressDialog("Progreso...", "Cancelar", 0, 100, self)

        #tiempo minimo del dialogo antes de cerrarse
        self.progressdialog.setMinimumDuration(0)


        #asignamos un titulo a la ventana del progressdialog
        self.progressdialog.setWindowTitle("progressdialog")


        self.botonIniciar = QPushButton('Iniciar Progreso', self)
        self.botonIniciar.clicked.connect(self.iniciarProgreso)

        layout = QVBoxLayout()
        layout.addWidget(self.botonIniciar)
        self.setLayout(layout)

    def iniciarProgreso(self):
        self.progreso = 0
        self.progressdialog.reset()  # Reiniciar el diálogo a su estado inicial

        #se le asigna el valor del progreso
        self.progressdialog.setValue(self.progreso)

        #se inicia o se muestra el progressdialog
        self.progressdialog.show()


        # Crear una instancia de QTimer asociada con la instancia actual de la clase
        self.temporizador = QTimer(self)
        # Conectar la señal 'timeout' del temporizador al método 'actualizarProgreso'
        self.temporizador.timeout.connect(self.actualizarProgreso)
        # Iniciar el temporizador con un intervalo de 100 milisegundos
        self.temporizador.start(100)#milisegundos

    def actualizarProgreso(self):

        if self.progressdialog.wasCanceled():
            self.temporizador.stop()
        else:
            self.progreso += 5
            self.progressdialog.setValue(self.progreso)
            if self.progreso >= 100:
                self.temporizador.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainProgressDialog()
    Window.show()
    sys.exit(app.exec())
