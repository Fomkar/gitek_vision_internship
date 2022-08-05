import sys
import cv2 as CV
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from WindowDesign import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        
        self.UI.rgb_color.clicked.connect(self.LoadRGB)
        self.UI.gray_color.clicked.connect(self.LoadGRAY)
        self.UI.bgr_color.clicked.connect(self.LoadBGR)
        self.pixel_array = CV.imread("McQueen.jpg")
        self.show()
    
    def ImageConverter(self, image, activate_gray = False):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        converted_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        if activate_gray == True:
            converted_image = converted_image.convertToFormat(QImage.Format_Grayscale8)
        image = converted_image.scaled(631, 351, Qt.KeepAspectRatio)
        return image
    
    def LoadRGB(self):
        rgb_pixels = CV.cvtColor(self.pixel_array, CV.COLOR_BGR2RGB)
        rgb_image = self.ImageConverter(rgb_pixels)
        self.pixmap = QPixmap.fromImage(rgb_image)
        self.UI.image.setPixmap(self.pixmap)
        
    def LoadGRAY(self):
        gray_pixels = CV.cvtColor(self.pixel_array, CV.COLOR_BGR2RGB)
        gray_image = self.ImageConverter(gray_pixels, True)
        self.pixmap = QPixmap(gray_image)
        self.UI.image.setPixmap(self.pixmap)
    
    def LoadBGR(self):
        bgr_image = self.ImageConverter(self.pixel_array)
        self.pixmap = QPixmap(bgr_image)
        self.UI.image.setPixmap(self.pixmap)

def StartApp():
    application = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(application.exec_())

StartApp()