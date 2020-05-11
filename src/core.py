from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

app = QApplication(sys.argv)  # Create a Window (not a Widget!)

class master(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(master, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.setAttribute(Qt.WA_TranslucentBackground, True) 
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        master.setWindowOpacity(0.25) # Thank you u/[deleted] https://www.reddit.com/r/learnpython/comments/3o4rdq/pyqt4_semitransparent_window/cvu98tk?utm_source=share&utm_medium=web2x
        self.show()

master = master()

sys.exit(app.exec_())