# -*- coding: utf-8 -*-
import os
import numpy as np
from scipy import misc
from imageio import imread
from imageio import imwrite
#from matplotlib.pyplot import imsave
#import matplotlib.image as mpimg

print('first')
filename1=input()
print('second')
filename2=input()
print('third')
outputfile=input()

im1=imread(filename1)
im2=imread(filename2)

w1=len(im1)
h1=len(im1[0])
w2=len(im2)
h2=len(im2[0])
print('width=',w1,'height=',h1, 'size=',h1*w1*4)
if w1>w2:
    w=w2
else:
    w=w1
if h1>h2:
    h=h2
else:
    h=h1
#im3=[i for i in range(0,w)]
im3=np.ones((w,h,3))
im1=im1.astype('uint8')
im2=im2.astype('uint8')
im3=im3.astype('uint8')
for ix in range (0,w):
    #im3[ix]=[i for i in range(o,h)]
    for iy in range(0,h):
        
        im3[ix][iy][0]=im1[ix][iy][0]
        im3[ix][iy][1]=im1[ix][iy][1]
        im3[ix][iy][2]=im1[ix][iy][2]
        
        if im2[ix][iy][0]==0:
            if im2[ix][iy][1]==0:
                if im2[ix][iy][2]==0:
                    im3[ix][iy]=[np.uint8(0),np.uint8(0),np.uint8(0)]
                """else:
                    im3[ix][iy][0]=im1[ix][iy][0]
                    im3[ix][iy][1]=im1[ix][iy][1]
                    im3[ix][iy][2]=im1[ix][iy][2]
                    #im3[ix][iy]=[np.uint8(im2[ix][iy][0]),np.uint8(im2[ix][iy][1]),np.uint8(im2[ix][iy][2])]
            else:
                im3[ix][iy][0]=im1[ix][iy][0]
                im3[ix][iy][1]=im1[ix][iy][1]
                im3[ix][iy][2]=im1[ix][iy][2]
                #im3[ix][iy]=[np.uint8(im2[ix][iy][0]),np.uint8(im2[ix][iy][1]),np.uint8(im2[ix][iy][2])]
        else:"""
"""
        im3[ix][iy][0]=im1[ix][iy][0]
        im3[ix][iy][1]=im1[ix][iy][1]
        im3[ix][iy][2]=im1[ix][iy][2]
            #im3[ix][iy]=[np.uint8(im2[ix][iy][0]),np.uint8(im2[ix][iy][1]),np.uint8(im2[ix][iy][2])]
"""

#imsave(outputfile,im3,format='bmp')
#imwrite(outputfile,im2,format='bmp')working
imwrite(outputfile,im3,format='bmp')
#misc.imsave(outputfile,im3)
#matplotlib.pyplot.imsave(outputfile,im3)

"""
Spyder Editor

This is a temporary script file.
"""












