
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QListWidget, 
                               QListWidgetItem, QCheckBox)
from PySide6.QtCore import Qt
import sys

def apply_dark_theme(app):
    # Define el estilo CSS para el tema oscuro
    dark_stylesheet = """
    * {
        background-color: #19232D;
        color: #F0F0F0;
    }
    QPushButton {
        background-color: #38414B;
        border-style: outset;
        border-width: 2px;
        border-color: #19232D;
        border-radius: 10px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #1ABC9C;
        color: #19232D;
    }
    QLineEdit {
        border: none;
        border-bottom: 1px solid gray;
        background-color: transparent;
        color: #F0F0F0;
        selection-background-color: #1ABC9C;
        selection-color: #F0F0F0;
    }
    """


    # Aplica el estilo CSS a la aplicación
    app.setStyleSheet(dark_stylesheet)

class MainWindow(QWidget):

    def __init__(self):

        pass

if __name__ == "_main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
