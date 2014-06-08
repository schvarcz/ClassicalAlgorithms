import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from numpy import matrix
from numpy.linalg import solve

#Gerar os pontos e aplicar uma equação-comportamento que deveremos descobrir
x = np.arange(0,100)
yr = 2*x+10
y = yr + randn(100)*10

#Gerar a representação SELA
A = matrix([x,np.ones(x.shape)]).T
b = matrix(y).T

#Resolver por LSE
i = solve(A.T*A,A.T*b).A1
print "A = {0} B = {1}".format(i[0],i[1])
yy = x*i[0]+i[1]
plt.plot(x,y,'o')
plt.show()

plt.plot(x,y,'o')
plt.plot(x,yy)
plt.plot(x,yr)
plt.show()



yr = x**2+x+10
y = yr + randn(100)*500

A = matrix([x**2,x,np.ones(x.shape)]).T
b = matrix(y).T

i = solve(A.T*A,A.T*b).A1
print i
print "A = {0} B = {1} C = {2}".format(i[0],i[1],i[2])
yy = i[0]*x**2+i[1]*x+i[2]
plt.plot(x,y,'o')
plt.show()

plt.plot(x,y,'o')
plt.plot(x,yy)
plt.plot(x,yr)
plt.show()



#x = np.arange(-100,100)
#yr = x**3 -100*x**2+x+10
yr = (x-20)**3-100*(x-20)**2-(x-20)
y = yr + randn(100)*10000

A = matrix([x**3,x**2,x,np.ones(x.shape)]).T
b = matrix(y).T

i = solve(A.T*A,A.T*b).A1
print i
print "A = {0} B = {1} C = {2} D = {3}".format(i[0],i[1],i[2],i[3])
yy = i[0]*x**3+i[1]*x**2+i[2]*x+i[3]
plt.plot(x,y,'o')
plt.show()

plt.plot(x,y,'o')
plt.plot(x,yy)
plt.plot(x,yr)
plt.show()
