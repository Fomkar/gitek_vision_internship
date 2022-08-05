import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from WindowDesign import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        
        self.UI.mcqueen.clicked.connect(self.LoadMcQueen)
        self.UI.optimus.clicked.connect(self.LoadOptimusPrime)
        
        self.show()
    
    def LoadMcQueen(self):
        self.pixmap = QPixmap("McQueen.jpg")
        self.UI.image.setPixmap(self.pixmap)
    
    def LoadOptimusPrime(self):
        self.pixmap = QPixmap("Optimus.jpg")
        self.UI.image.setPixmap(self.pixmap)

def StartApp():
    application = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    application.exec()

StartApp()