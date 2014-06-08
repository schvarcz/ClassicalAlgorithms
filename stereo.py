from cv2 import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots,cm

imgl, imgr = cvtColor(imread("I1_000000.png"),cv.CV_RGBA2GRAY),
             cvtColor(imread("I2_000000.png"),cv.CV_RGBA2GRAY)

ste = StereoSGBM(0,96,11,8*11*11,32*11*11)

disp = ste.compute(imgl,imgr)/16.

f,(a4) = subplots(1)

#Foco da camera * distância entre as duas imagens
dist = 6.452401e+02*.57073824147/disp
im1 = a4.imshow(dist)
im1.set_clim(0.,64)
plt.colorbar(im1)

plt.show()




