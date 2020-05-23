#!/usr/bin/env python3
# pylint: disable=E0602
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
print("Success! import PyQt5")
from time import strftime
import sys
from fugai import *
print("Success! import other dependencies.")

class clockView(QWidget): # H/t https://www.geeksforgeeks.org/pyqt5-create-a-digital-clock/
    def __init__(self, parent=None, *args, **kwargs):
        super(clockView, self).__init__(*args, **kwargs)
        self.setGeometry(0, 0, 500, 100)
        font = QFont(global_font, 100, QFont.Bold)
        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setFont(font)

        layout.addWidget(self.label)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.clockBuild)
        timer.start(1000)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog) # H/t https://stackoverflow.com/questions/50892264/pyqt4-how-keep-a-qwidget-always-on-top
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()
        self.show()
    def clockBuild(self, parent=None):
        timeNow = QTime.currentTime()
        timeString = timeNow.toString('hh:mm:ss')
        self.label.setText(timeString)


