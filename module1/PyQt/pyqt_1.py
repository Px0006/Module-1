import sys
from  PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("Window")
    w.show()
    sys.exit(app.exec_())

window()


