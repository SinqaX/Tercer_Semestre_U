import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader


def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")

if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("expo.ui", None)
    mainwindow_setup(window)
    window.show()
    app.exec()