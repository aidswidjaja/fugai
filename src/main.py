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
print("[Success!] main.py import PyQt5")
import sys
from fugai import *
from clockview import clockView
sys.path.insert(1, '/ashbadger/browser_tabbed.py')
from browser_tabbed import *
print("[Success!] main.py import other dependencies.")

app = QApplication(sys.argv)
print("[Success!] main.py sys.argv")

class master(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(master, self).__init__(*args, **kwargs)
        self.setWindowTitle("Fugai")
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
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
    # webMainWindow = webMainWindow()
    # print("Success! webMainWindow()")
    sys.exit(app.exec_())
