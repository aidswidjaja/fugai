#!/usr/bin/env python3
# pylint: disable=E0602
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
print("Success! import PyQt5")
from time import strftime
import qtmodern.styles
import qtmodern.windows
import sys
from fugai import *
from localtime import clockView
print("Success! import other dependencies.")

app = QApplication(sys.argv)
print("Success! sys.argv")

class master(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(master, self).__init__(*args, **kwargs)
        self.setWindowTitle("Fugai")
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnBottomHint |
            Qt.WindowDoesNotAcceptFocus |
            Qt.X11BypassWindowManagerHint)
        self.setWindowOpacity(opacity)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet("background-color: "+ background_colour +"; background-image: url("+ background_image +"); background-repeat: no-repeat; background-position: center;")
        self.showMaximized()


if __name__ == '__main__':
    master = master()
    print("Success! master()")
    clockView = clockView(master)
    print("Success! clockView()")
    sys.exit(app.exec_())