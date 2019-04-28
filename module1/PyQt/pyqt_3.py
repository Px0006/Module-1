# PyQt5 window with a button


import sys
from  PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Hello')
    l.setText('look at me')
    w.setWindowTitle("Boobs")
    b.move(100, 50)
    l.move(110, 100)
    w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())

window()
