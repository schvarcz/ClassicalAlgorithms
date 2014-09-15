from numpy import *
from matplotlib import pyplot as plt

class Neuron():

    def __init__(self, dimensions, learningRate = 0.005):
        self.w = random.rand(dimensions+1)
        self.n = learningRate

    def train(self, data):
        swapped = True
        era = 0

        while swapped:
            swapped = False
            for values,group in data:
                values = asarray(values)
                u = self.w*values
                y = self.activation(u.sum())
                if group != y:
                    swapped = True
                    self.w += self.n*(group-y)*values
            era += 1

    def activation(self,signal):
        if signal > 0:
            return 1
        else:
            return -1

    def classify(self,pt):
        return self.activation((self.w*pt).sum())

#Samples
pts1 = random.randn(10,2)*5+ asarray([30,-10])
pts2 = random.randn(10,2)*5+ asarray([10,0])

x, y = zip(*pts1)
plt.plot(x,y,"bo")

x, y = zip(*pts2)
plt.plot(x,y,"ro")
plt.show()
x, y = zip(*pts1)
plt.plot(x,y,"bo")

x, y = zip(*pts2)
plt.plot(x,y,"ro")

#Training
neuron = Neuron(2)

bias = [-1 for c in x]
x,y = zip(*pts1)
d = zip(zip(bias,x,y),[1 for c in x])
x,y = zip(*pts2)
d += zip(zip(bias,x,y),[-1 for c in x])

neuron.train(d)

#Classification
pts1 = random.rand(10,2)*asarray([40,3])
conj1 = []
conj2 = []
for pt in pts1:
    pt = [-1]+pt.tolist()
    if neuron.classify(pt) >0:
        conj1.append(pt)
    else:
        conj2.append(pt)

if conj1 != []:
    b, x,y = zip(*conj1)
    plt.plot(x,y,"yo")

if conj2 != []:
    b, x,y = zip(*conj2)
    plt.plot(x,y,"go")

x = arange(-20,40)
y = neuron.w[0]/neuron.w[2] -x*neuron.w[1]/neuron.w[2]
plt.plot(x,y)
plt.show()

