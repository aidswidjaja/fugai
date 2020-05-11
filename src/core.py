from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
print("Success! import PyQt5")

import qtmodern.styles
import qtmodern.windows
import sys
print("Success! import other dependencies.")

app = QApplication(sys.argv)  # Create a Window (not a Widget!)
print("Success! sys.argv")

class master(QDialog):
    def __init__(self, *args, **kwargs):
        super(master, self).__init__(*args, **kwargs)
        self.setWindowTitle("Fugai")
        print("Success! setWindowTitle")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.8) # Thank you u/[deleted] https://www.reddit.com/r/learnpython/comments/3o4rdq/pyqt4_semitransparent_window/cvu98tk?utm_source=share&utm_medium=web2x
        self.setStyleSheet("background-color: #07071f") # Thank you Alvaro Fuentes https://stackoverflow.com/questions/20668060/pyqt-qpushbutton-background-color
        self.show()
        print("Success! show()")

master = master()
print("Success! Mainloop")

#qtmodern.styles.dark(app)
#mw = qtmodern.windows.ModernWindow(master)
#print("Success! Generate ModernWindow")
#mw.show()
#print("Success! show() ModernWindow")

sys.exit(app.exec_())
print("Success! Program terminated.")