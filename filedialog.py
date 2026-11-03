import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog

class FileOpenDialog(QWidget):
    def __init__(self):
        super().__init__()
    def openFileNameDialog(self):
        fileName,_ = QFileDialog.getOpenFileName(self,caption='Find Image',directory='C:/Users/p/Desktop/My Python/Projects/3-Store_APP Project/pic',filter='All Image Files(*.jpg, *.png);;JPG(*.jpg);;PNG(*.png);;')
        if fileName:
            return fileName
        else:
            return None
        