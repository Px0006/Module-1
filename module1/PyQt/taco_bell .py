# signals and slots

import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b1 = QtWidgets.QPushButton('Taco')
        self.l1 = QtWidgets.QLabel('How are they made?')

        self.b2 = QtWidgets.QPushButton('Taco Supreme')
        self.l2 = QtWidgets.QLabel('How is it made?')

        self.b3 = QtWidgets.QPushButton('DLT')
        self.l3 = QtWidgets.QLabel('How is it made?')

        self.b4 = QtWidgets.QPushButton('DLT Supreme')
        self.l4 = QtWidgets.QLabel('How is it made?')

        self.b5 = QtWidgets.QPushButton('Shreded Chicken Taco')
        self.l5 = QtWidgets.QLabel('How is it made?')

        self.b6 = QtWidgets.QPushButton('Grilled Steak')
        self.l6 = QtWidgets.QLabel('How is it made?')

        self.b7 = QtWidgets.QPushButton('Spicy Potato')
        self.l7 = QtWidgets.QLabel('How is it made?')

        self.b8 = QtWidgets.QPushButton('Double Decker')
        self.l8 = QtWidgets.QLabel('How is it made?')

        self.b9 = QtWidgets.QPushButton('Double Decker Supreme')
        self.l9 = QtWidgets.QLabel('How is it made?')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l1)
        h_box.addWidget(self.l2)
        h_box.addWidget(self.l3)
        h_box.addWidget(self.l4)
        h_box.addWidget(self.l5)
        h_box.addWidget(self.l6)
        h_box.addWidget(self.l7)
        h_box.addWidget(self.l8)
        h_box.addWidget(self.l9)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.b3)
        v_box.addWidget(self.b4)
        v_box.addWidget(self.b5)
        v_box.addWidget(self.b6)
        v_box.addWidget(self.b7)
        v_box.addWidget(self.b8)
        v_box.addWidget(self.b9)                                                                        
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Taco Bell')

        self.b1.clicked.connect(self.btn_click)
        self.b2.clicked.connect(self.btn_click)
        self.b3.clicked.connect(self.btn_click)
        self.b4.clicked.connect(self.btn_click)
        self.b5.clicked.connect(self.btn_click)
        self.b6.clicked.connect(self.btn_click)
        self.b7.clicked.connect(self.btn_click)
        self.b8.clicked.connect(self.btn_click)
        self.b9.clicked.connect(self.btn_click)
        self.show()

    def btn_click(self):
        self.l1.setText('A tortila, meat, lettuce, and cheese')
        self.l2.setText('A tortila, beef, sour cream, lettuce, and cheddar, tomato')
        self.l3.setText('A tortila, meat, lettuce, and cheese')
        self.l4.setText('A tortila, meat, lettuce, and cheese')
        self.l5.setText('A tortila, meat, lettuce, and cheese')
        self.l6.setText('A tortila, meat, lettuce, and cheese')
        self.l7.setText('A tortila, meat, lettuce, and cheese')
        self.l8.setText('A tortila, meat, lettuce, and cheese')
        self.l9.setText('A tortila, meat, lettuce, and cheese')

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
