from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)  # Config setup based on OS
    window = QMainWindow()
    xpos = 200
    ypos = 200
    width = 300
    height = 300
    window.setGeometry(xpos, ypos, width, height)
    window.setWindowTitle("Hello Tagungsuhr!")

    label = QtWidgets.QLabel(window)
    label.setText("Erste Überschrift")
    label.move(50, 50)

    window.show()
    sys.exit(app.exec_())  # Wait for Programm to exit

window()