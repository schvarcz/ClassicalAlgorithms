#-*- coding: utf8 -*-
from cv2 import imread
import numpy as np
from math import pow,log


def bhattacharyya(template,comp,bins=None):
    if bins == None:
        bins == 130
    hTemplate = np.histogram(template,bins)
    hComp = np.histogram(comp,bins)
    return -log(np.sqrt(hTemplate[0]*hComp[0]).sum())
    
if __name__ == "__main__":
    frame = imread("frame.png")
    rank = []
    for i in range(10):
        template = imread("template_{}.png".format(i))
        rank.append((bhattacharyya(template,frame,128),"template_{}.png".format(i)))
    print sorted(rank)
    
    
    
