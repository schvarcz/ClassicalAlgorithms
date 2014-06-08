#-*- coding: utf8 -*-
from cv2 import imread
import numpy as np


def ssd(template,comp):
    sd = np.power(comp-template,2)
    return sd.sum()
    
def sad(template,comp):
    sd = comp-template
    return sd.sum()
    
if __name__ == "__main__":
    frame = imread("frame.png")
    rank = []
    for i in range(10):
        template = imread("template_{}.png".format(i))
        rank.append((ssd(template,frame),"template_{}.png".format(i)))
    print sorted(rank)



