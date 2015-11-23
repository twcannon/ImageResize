# -*- coding: utf-8 -*-
'''
A Program to resize all images of the same
file type within a given directory
Author: Thomas Cannon
Free to share/use/whatever ...I dont care :D

        !!!!!WORD OF CAUTION!!!!!

THIS PROGRAM WILL WRITE OVER YOUR EXISTING FILES!
    MAKE A COPY OF THE FILES THAT YOU ARE 
            RESIZING BEFORE USE!
    
        !!!!!WORD OF CAUTION!!!!!
        
        
'''
#####################
#####  IMPORTS  #####
#####################
import os
import numpy as np 
import Image
import PIL.Image


###################################
#####  THINGS YOU CAN CHANGE  #####
###################################
imgType = ".png"
atleast = 1600    # atleast is the minimum height or width that you want the picture to have in pixels
rootDir = '/Path/To/Directory'    # rootDir should be changes to the root folder where your images are stored.
# All images of the specified image file type within this directory will be affected.


###################################
#####  THE RESIZING FUNCTION  #####
###################################
def image_resize(image,atleast):
    img = Image.open(image)
    widthOrHeight = np.argmax(img.size)
    if max(img.size) < atleast:
        #widthOrHeight = 0 #uncomment this to set all widths to atleast number of pixels
        #widthOrHeight = 1 #uncomment this to set all heights to atleast number of pixels
        if widthOrHeight == 0:
            basewidth = atleast
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((int(basewidth), hsize), PIL.Image.ANTIALIAS)
        elif widthOrHeight == 1:
            baseheight = atleast
            wpercent = (baseheight / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(wpercent)))
            img = img.resize((wsize, int(baseheight)), PIL.Image.ANTIALIAS)
    img.save(image)
    return


################################
#####  THE DIRECTORY LOOP  #####
################################
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.endswith(imgType):
            print fname
            image_resize(dirName+'/'+fname, atleast)
                
print 'Done'