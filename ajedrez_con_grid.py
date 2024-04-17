from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtCore
import math
import os
import sys

# problemas con el promedio
# elevacion volverla mas dinamica
#controlar division /0


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        basedir = os.path.dirname(__file__)

        layout_padre = QGridLayout()
        
        self.setWindowTitle("Calculadora")
        Icon = QIcon(os.path.join(basedir,"img","icon.png"))
        self.setWindowIcon(Icon)
        
        for i in range(8):
            for j in range(8):
                widget = QWidget()
                label = QLabel(widget)
                widget.setAutoFillBackground(True)
                palette = widget.palette()
                if (i + j) % 2 == 0:
                    palette.setColor(QPalette.Window, Qt.black)
                    palette.setColor(QPalette.WindowText, Qt.white)
                else:
                    palette.setColor(QPalette.Window, Qt.white)
                    palette.setColor(QPalette.WindowText, Qt.black)
                widget.setPalette(palette)
                widget.setMinimumSize(50, 50)
                label.setText(f"{i}, {j}")
                layout_padre.addWidget(widget, i, j)
                layout_padre.addWidget(label, i, j)
                layout_padre.setSpacing(0)

        
        self.setLayout(layout_padre)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
