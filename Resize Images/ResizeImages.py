from pathlib import Path
import glob
import numpy as np
import cv2
def resizeImage(image, scale=0.50):
    width=int(image.shape[1]*scale)
    height=int(image.shape[0]*scale)
    
    dimension=(width,height)
    return cv2.resize(image,dimension)
img_list=glob.glob('D:\pictures\*.*')

for img in img_list:
    image=cv2.imread(img)
    new_Image=resizeImage(image,0.50)
    cv2.imwrite("D:\\saveFolder\\" + Path(img).stem +"_jumatate.jpg",new_Image)