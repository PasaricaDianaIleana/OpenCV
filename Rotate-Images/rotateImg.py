
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage,QTransform
import sys
import cv2
import numpy as np

class Ui_MainWindow(QMainWindow):
    imageOpenCV = None

    def setupUi(self, MainWindow):
      
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openImage = QtWidgets.QPushButton(self.centralwidget)
        self.openImage.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.openImage.setObjectName("openImage")
        self.labelPic = QtWidgets.QLabel(self.centralwidget)
        self.labelPic.setGeometry(QtCore.QRect(60, 90, 691, 441))
        self.labelPic.setText("")
        self.labelPic.setObjectName("labelPic")
        
        self.openImage.clicked.connect(self.getImage)
        
        self.rotateImg = QtWidgets.QPushButton(self.centralwidget)
        self.rotateImg.setGeometry(QtCore.QRect(200, 30, 93, 28))
        self.rotateImg.setObjectName("rotateImg")
        self.rotateImg.clicked.connect(self.rotateImage)
        
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(380, 30, 93, 28))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.saveImage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def getImage(self):
        filePath = QFileDialog.getOpenFileName(self, "Open file", "D:\\", "*.jpg *.jpeg *.gif")
        self.filePath = filePath[0];
        self.imageOpenCV = cv2.imread(self.filePath)
        print(self.imageOpenCV)
        pixmap = QPixmap(filePath[0])
        self.labelPic.setPixmap(pixmap.scaled(self.labelPic.size()))
        
    def saveImage(self):
        img=self.imageOpenCV.copy()
        cv2.imwrite('D://cat.jpg',img)
     
    def rotateImage(self):
        img=self.imageOpenCV.copy()
        newImg=self.updateImg(img)
        imageReady = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
        h, w, _ = imageReady.shape
        self.pixmap=QImage(imageReady.data,w,h, QImage.Format_RGB888)
        self.labelPic.setPixmap(QPixmap(self.pixmap).scaled(self.labelPic.size()))
        
    def updateImg(self,img):
        new_img=cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        self.imageOpenCV = new_img
        return new_img
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openImage.setText(_translate("MainWindow", "Open"))
        self.rotateImg.setText(_translate("MainWindow", "Rotate"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app= QtWidgets.QApplication(sys.argv)
        
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    app.exec_()
    app.quit()


