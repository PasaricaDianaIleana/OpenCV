#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage,QTransform
import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt

class Ui_MainWindow(object):
    initialImg=None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.loadWebCamBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadWebCamBtn.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.loadWebCamBtn.setObjectName("loadWebCamBtn")
        
        self.loadWebCamBtn.clicked.connect(self.openWebCam)
        
        self.kernelSlider = QtWidgets.QSlider(self.centralwidget)
        self.kernelSlider.setGeometry(QtCore.QRect(40, 130, 541, 22))
        self.kernelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kernelSlider.setObjectName("kernelSlider")
        self.kernelSlider.setMaximum(25)
        self.kernelSlider.setValue(3)
        self.kernelSlider.valueChanged.connect(self.changeKernelSize)
        
        
        
        self.sigmaSlider = QtWidgets.QSlider(self.centralwidget)
        self.sigmaSlider.setGeometry(QtCore.QRect(40, 200, 541, 22))
        self.sigmaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sigmaSlider.setObjectName("sigmaSlider")
        self.sigmaSlider.setMaximum(2000)
        self.sigmaSlider.setValue(0.1)
        self.sigmaSlider.valueChanged.connect(self.changeSigmaValue)
        
        self.sigmaColorSlider = QtWidgets.QSlider(self.centralwidget)
        self.sigmaColorSlider.setGeometry(QtCore.QRect(40, 270, 541, 22))
        self.sigmaColorSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sigmaColorSlider.setObjectName("sigmaColorSlider")
        self.sigmaColorSlider.setMaximum(2000)
        self.sigmaColorSlider.setValue(0.1)
        self.sigmaColorSlider.valueChanged.connect(self.changeSigmaColorValue)
        self.kernelLbl = QtWidgets.QLabel(self.centralwidget)
        self.kernelLbl.setGeometry(QtCore.QRect(610, 130, 55, 16))
        self.kernelLbl.setText("Kernel")
        self.kernelLbl.setObjectName("kernelLbl")
        self.sigmaLbl = QtWidgets.QLabel(self.centralwidget)
        self.sigmaLbl.setGeometry(QtCore.QRect(620, 200, 55, 16))
        self.sigmaLbl.setText("Sigma")
        self.sigmaLbl.setObjectName("sigmaLbl")
        self.sigmaColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.sigmaColorLbl.setGeometry(QtCore.QRect(620, 270, 55, 16))
        self.sigmaColorLbl.setText("Sigma color")
        self.sigmaColorLbl.setObjectName("sigmaColorLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def openWeb(self):
        img = cv2.VideoCapture()
        img.open(0, cv2.CAP_DSHOW)
        while(True):
            ret, frame = img.read()
            grayScaleImg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            self.updateImages(updateImages)
            for x in range(1,9,1):
                self.applyFilter(grayScaleImg,x)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        img.release()
        cv2.destroyAllWindows()
    
    def openWebCam(self):
        self.openWeb()
    
        
    def BlurImage(self,frame):
        Img=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        blur5 = cv2.blur(Img, (20, 20))
        cv2.imshow('blur img',blur5)
        
    def applyFilter(self,frame,number, kernelSize,sigma, sigmaCol):
        if number == 1:
            Img=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            blurImg = cv2.blur(Img, (kernelSize, kernelSize))
            cv2.imshow('blur img',blurImg)
        elif number == 2:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gausImg = cv2.GaussianBlur(img,(kernelSize,kernelSize),sigma)
            cv2.imshow('gaus img',gausImg)
        elif number == 3:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            medianFiltre = cv2.medianBlur(img, kernelSize)
            cv2.imshow('median img',medianFiltre)
        elif number == 4:
            sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, kernelSize)
            cv2.imshow('sobel orizontala',sobelx)
        elif number == 5:
            sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1, kernelSize)
            cv2.imshow('sobel verticala',sobely)
        elif number == 6:    
            laplacian = cv2.Laplacian(frame, cv2.CV_64F)
            cv2.imshow('laplacian',laplacian)
        elif number == 7:
            bilateral = cv2.bilateralFilter(frame, kernelSize, sigmaCol, sigma)
            cv2.imshow('bilateral',bilateral)
        elif number == 8:    
            edges = cv2.Canny(frame, 100, 200)
            cv2.imshow('canny',edges)
        else:
            print('no image')   
            
    
    def changeKernelSize(self):
        value = self.kernelSlider.value() 
        kernelSize = value * 2 + 1
        if  value<=15 :
            sobelKernelSize = value * 2 + 1
        else:
             sobelKernelSize = 31
        self.kernelLbl.setText('Kernel:' + int(sobelKernelSize))
        
    def changeSigmaValue(self):    
        value = self.sigmaSlider.value() 
        sigma = float(value)/10;
        self.sigmaLbl.setText('sigma:' + float(sigma))
    def updateImages(self,img):
        print('update values')
        
    def changeSigmaColorValue(self):
        value = self.sigmaColorSlider.value() 
        sigmaColor = float(value)/10;
        self.sigmaColorLbl.setText('sigma color:' + float(sigmaColor))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadWebCamBtn.setText(_translate("MainWindow", "Start WebCam"))
    
    
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


# In[ ]:




