"""
2020 (c) aidswidjaja 
https://aidswidjaja.github.io

This program is free software: you can redistribute it and/or modify
it under the terms of the MIT License as originally published by
the Massachusetts Institute of Technology and currently maintained by
the Open Source Initiative.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
MIT License for more details.

You should have received a copy of the MIT License
along with this program.  If not, see <https://opensource.org/licenses/MIT>.
"""

#!/usr/bin/env python3
# pylint: disable=E0602
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
print("[Success!] clockview.py import PyQt5")
import sys
from fugai import *
print("[Success!] clocview.py import other dependencies.")

class clockView(QWidget): # H/t https://www.geeksforgeeks.org/pyqt5-create-a-digital-clock/
    def __init__(self, parent=None, *args, **kwargs):
        super(clockView, self).__init__(*args, **kwargs)
        self.setGeometry(0, 0, 500, 100)
        font = QFont(clock_font, clock_font_size, QFont.Bold)
        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setFont(font)
        self.label.setStyleSheet("color: "+ clock_font_colour +";")

        layout.addWidget(self.label)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.clockBuild)
        timer.start(1000)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Dialog)  # H/t https://stackoverflow.com/questions/50892264/pyqt4-how-keep-a-qwidget-always-on-top
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: transparent;")
        self.setFocusPolicy(Qt.StrongFocus)
        self.show()

    def clockBuild(self=None):
        timeNow = QTime.currentTime()
        timeString = timeNow.toString('hh:mm:ss')
        self.label.setText(timeString)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def closeEvent(self, event):
        self.settings = QSettings("Nettomo", "Fugai")
        self.settings.setValue("geometry", saveGeometry())
        self.settings.setValue("windowState", saveState())
        self.closeEvent(event)

    def readSettings(self):
        self.settings = QSettings("Nettomo", "Fugai")
        self.settings = QSettings("Nettomo", "Fugai")
        self.settings.value("geometry")
        self.restoreGeometry(geometry)
    
    # H/t https://stackoverflow.com/a/37718648/6299634
    # Credit: Elad Joseph