import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from random import *
from math import *

pts = []

#Cria os pontos
x = randn(4,2)*100
for j in range(4):
    pts += (randn(50,2)*10 + x[j]).tolist()

x, y = zip(*pts)
plt.scatter(x, y)
plt.show()


k = 4
centroids = []
for i in range(k):
#    centroids.append([randint(0,100),randint(0,100)])
    centroids.append(pts[randint(0,len(pts))])

def distancia(c,p):
    return sqrt( (p[0] - c[0])**2 + (p[1] - c[1])**2 )



for q in range(20):

    clusters = [[] for i in range(k)]
    for p in pts:
        index = -1
        for c in range(len(centroids)):
            if index == -1:
                index = c
            else:
                if distancia(centroids[c],p) < distancia(centroids[index],p):
                    index = c
        clusters[index].append(p)
        
    for i in range(4):
        print len(clusters[i])

    s = zip(*centroids)
    plt.scatter(s[0],s[1],color='k')

    if len(clusters[0]) != 0:
        s = zip(*clusters[0])
        centroids[0] = [np.asarray(s[0]).mean(),np.asarray(s[1]).mean()]
        plt.scatter(s[0],s[1],color='y')

    if len(clusters[1]) != 0:
        s = zip(*clusters[1])
        centroids[1] = [np.asarray(s[0]).mean(),np.asarray(s[1]).mean()]
        plt.scatter(s[0],s[1],color='r')

    if len(clusters[2]) != 0:
        s = zip(*clusters[2])
        centroids[2] = [np.asarray(s[0]).mean(),np.asarray(s[1]).mean()]
        plt.scatter(s[0],s[1],color='g')

    if len(clusters[3]) != 0:
        s = zip(*clusters[3])
        centroids[3] = [np.asarray(s[0]).mean(),np.asarray(s[1]).mean()]
        plt.scatter(s[0],s[1],color='c')

    plt.show()
