#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QColorDialog
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import cv2
import random

class Ui_MainWindow(QMainWindow):
    initialImg=None
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(30, 30, 93, 28))
        self.openButton.setObjectName("openButton")
        self.openButton.clicked.connect(self.getImage)
        
        self.scaleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scaleBtn.setGeometry(QtCore.QRect(180, 30, 93, 28))
        self.scaleBtn.setObjectName("scaleBtn")
        self.scaleBtn.clicked.connect(self.changeScale)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 910, 351, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setValue(120)
        self.horizontalSlider.valueChanged.connect(self.minValueChange)
       
        
        self.minSliderLabel = QtWidgets.QLabel(self.centralwidget)
        self.minSliderLabel.setGeometry(QtCore.QRect(120, 940, 49, 16))
        self.minSliderLabel.setText("120")
        self.minSliderLabel.setObjectName("minSliderLabel")
        
        
        self.maxHorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.maxHorizontalSlider.setGeometry(QtCore.QRect(470, 910, 351, 22))
        self.maxHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxHorizontalSlider.setObjectName("maxHorizontalSlider")
        self.maxHorizontalSlider.setMaximum(255)
        self.maxHorizontalSlider.setValue(255)
        self.maxHorizontalSlider.valueChanged.connect(self.maxValueChange)
       
        
        self.maxSliderLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxSliderLabel.setGeometry(QtCore.QRect(500, 940, 249, 16))
        self.maxSliderLabel.setText("255")
        self.maxSliderLabel.setObjectName("maxSliderLabel")
        
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(330, 30, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveFiles)
        
        
        self.initImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.initImgLabel.setGeometry(QtCore.QRect(60, 150, 355, 316))
        self.initImgLabel.setText("")
        self.initImgLabel.setObjectName("initImgLabel")
        
        self.grayImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.grayImgLabel.setGeometry(QtCore.QRect(500, 150, 355, 316))
        self.grayImgLabel.setText("")
        self.grayImgLabel.setObjectName("grayImgLabel")
        
        self.binaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.binaryLabel.setGeometry(QtCore.QRect(950,150, 355, 316))
        self.binaryLabel.setText("binaryLabel")
        self.binaryLabel.setObjectName("binaryLabel")
        
        self.binaryInvLabel = QtWidgets.QLabel(self.centralwidget)
        self.binaryInvLabel.setGeometry(QtCore.QRect(1450,150, 355, 316))
        self.binaryInvLabel.setText("binaryInvLabel")
        self.binaryInvLabel.setObjectName("binaryInvLabel")
        
        self.truncLabel = QtWidgets.QLabel(self.centralwidget)
        self.truncLabel.setGeometry(QtCore.QRect(60, 510, 355, 316))
        self.truncLabel.setText("truncLabel")
        self.truncLabel.setObjectName("truncLabel")
        
        self.tozeroLabel = QtWidgets.QLabel(self.centralwidget)
        self.tozeroLabel.setGeometry(QtCore.QRect(500, 510, 355, 316))
        self.tozeroLabel.setText("")
        self.tozeroLabel.setObjectName("tozeroLabel")
        
        self.tozeroInvLabel = QtWidgets.QLabel(self.centralwidget)
        self.tozeroInvLabel.setGeometry(QtCore.QRect(950, 510, 355, 316))
        self.tozeroInvLabel.setText("")
        self.tozeroInvLabel.setObjectName("tozeroInvLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 26))
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
        global name
        self.initialImg=cv2.imread(self.filePath)
        name=Path(filePath[0]).stem
        pixmap = QPixmap(filePath[0])
        self.initImgLabel.setPixmap(pixmap.scaled(self.initImgLabel.size()))
      
    def changeScale(self):
        img=self.initialImg.copy()
        global new_img
        new_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h,w= new_img.shape
        self.pixmap=QImage(new_img.data, w, h, w, QImage.Format_Grayscale8)
        self.grayImgLabel.setPixmap(QPixmap(self.pixmap).scaled(self.grayImgLabel.size()))
        self.updateImages()
        
   
    def handle(self,image,number,minVal,maxVal):
        if number == 1:
            ret,thresh1 = cv2.threshold(image,minVal,maxVal,cv2.THRESH_BINARY)
            image_array.append(thresh1)
            h,w = thresh1.shape
            self.pixmap=QImage(thresh1.data, w, h, w, QImage.Format_Grayscale8)
            self.binaryLabel.setPixmap(QPixmap(self.pixmap).scaled(self.binaryLabel.size())),
           
        elif number == 2:
            ret,thresh2 = cv2.threshold(image,minVal,maxVal,cv2.THRESH_BINARY_INV)
            h,w = thresh2.shape
            image_array.append(thresh2)
            self.pixmap=QImage(thresh2.data, w, h, w, QImage.Format_Grayscale8)
            self.binaryInvLabel.setPixmap(QPixmap(self.pixmap).scaled(self.binaryInvLabel.size())),
            
        elif number == 3:
            ret,thresh3 = cv2.threshold(image,minVal,maxVal,cv2.THRESH_TRUNC)
            h,w = thresh3.shape
            image_array.append(thresh3)
            self.pixmap=QImage(thresh3.data, w, h, w, QImage.Format_Grayscale8)
            self.truncLabel.setPixmap(QPixmap(self.pixmap).scaled(self.truncLabel.size())),
            
        elif number == 4:
            ret,thresh4 = cv2.threshold(image,minVal,maxVal,cv2.THRESH_TOZERO)
            h,w = thresh4.shape
            image_array.append(thresh4)
            self.pixmap=QImage(thresh4.data, w, h, w, QImage.Format_Grayscale8)
            self.tozeroLabel.setPixmap(QPixmap(self.pixmap).scaled(self.tozeroLabel.size())),
        
        elif number == 5:
            ret,thresh5 = cv2.threshold(image,minVal,maxVal,cv2.THRESH_TOZERO_INV)
            h,w = thresh5.shape
            image_array.append(thresh5) 
            self.pixmap=QImage(thresh5.data, w, h, w, QImage.Format_Grayscale8)
            self.tozeroInvLabel.setPixmap(QPixmap(self.pixmap).scaled(self.tozeroInvLabel.size())),
        else:
            print('no image')
            
    def minValueChange(self):
        value = self.horizontalSlider.value()
        self.minSliderLabel.setText(str(value))
        self.updateImages()
    
    def maxValueChange(self):
        value = self.maxHorizontalSlider.value() 
        self.maxSliderLabel.setText(str(value))
        self.updateImages()
        
    def updateImages(self):
        global image_array
        image_array=[]
        minVal = int(self.minSliderLabel.text())
        maxVal = int(self.maxSliderLabel.text())
        for x in range(1,6,1):
            self.handle(new_img,x,minVal,maxVal)
           
            
            
    def saveFiles(self):
        i=0
        imgName=['_binary','_binary_inv','_trunc','_tozero','_tozero_inv']
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        for image in image_array:
            if i<=4:
                cv2.imwrite(folderpath[0]+'://'+name+imgName[i]+'.jpg', image)
                i=i+1
                
           
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open"))
        self.scaleBtn.setText(_translate("MainWindow", "Gray scale"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.initImgLabel.setText(_translate("MainWindow", ""))
        self.grayImgLabel.setText(_translate("MainWindow", ""))
        self.binaryLabel.setText(_translate("MainWindow", "binaryLabel"))
        
        self.binaryInvLabel.setText(_translate("MainWindow", "binaryInvLabel"))
        self.truncLabel.setText(_translate("MainWindow", "truncLabel")) 
        self.tozeroLabel.setText(_translate("MainWindow", "tozeroLabel")) 
        self.tozeroInvLabel.setText(_translate("MainWindow", "tozeroInvLabel")) 

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)

 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    app.exec_()
    app.quit()






# In[ ]:




