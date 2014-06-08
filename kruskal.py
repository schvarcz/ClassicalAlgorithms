#-*- coding: utf8 -*-
from numpy import *
from numpy.random import *
from matplotlib import pyplot as plt

def hashlist(l):
    return ','.join([str(i) for i in l])

def distancia(pt1,pt2):
    return sqrt(pow(pt2[0]- pt1[0],2)+pow(pt2[1]- pt1[1],2))

#Dados de entrada
vertices = randn(20,2).tolist()
vertices += (randn(20,2) + asarray([5,5])).tolist()
vertices += (randn(20,2) + asarray([-5,5])).tolist()
vertices += (randn(20,2) + asarray([-5,-5])).tolist()
vertices += (randn(20,2) + asarray([5,-5])).tolist()

k = 5
x, y = zip(*vertices)
plt.plot(x,y,'o')
plt.show()

#Construção do grafo completo
arestas = []
for pt in vertices:
    for l in vertices:
        if l != pt:
            arestas.append([pt,l])

for aresta in arestas:
    x,y = zip(*aresta)
    plt.plot(x,y,'r')

x, y = zip(*vertices)
plt.plot(x,y,'bo')
plt.show()

#Algoritimo de Kruskal para se extrair a árvore geradora mínima
arestas = sorted(arestas,key= lambda l: distancia(l[0],l[1]))
arvoreGeradora = []
sets = []

for aresta in arestas:
    index = [-1, -1]

    for s in range(len(sets)):
        for i in range(2):
            if aresta[i] in sets[s]:
                index[i] = s

    if (index[0] != index[1]) or (index[0] == index[1] == -1):
        arvoreGeradora.append(aresta)
        if index[0] == index[1] == -1:
            sets.append([aresta[0],aresta[1]])
        elif index[0] == -1:
            sets[index[1]].append(aresta[0])
        elif index[1] == -1:
            sets[index[0]].append(aresta[1])
        else:
            set1, set2 = sets[index[0]], sets[index[1]]
            sets.remove(set1)
            sets.remove(set2)
            sets.append(set1 + set2)

for aresta in arvoreGeradora:
    x,y = zip(*aresta)
    plt.plot(x,y,'r')

for s in sets:
    x, y = zip(*s)
    plt.plot(x,y,'o')
plt.show()


#Segmentação da árvore em componentes k grupos
for i in range(k-1):
    arvoreGeradora.remove(arvoreGeradora[-1])

for aresta in arvoreGeradora:
    x,y = zip(*aresta)
    plt.plot(x,y,'r')


#Apenas para separar os set's dos pontos de forma a colorir diferentemente
sets = []
for aresta in arvoreGeradora:
    index = [-1, -1]

    for s in range(len(sets)):
        for i in range(2):
            if aresta[i] in sets[s]:
                index[i] = s

    if (index[0] != index[1]) or (index[0] == index[1] == -1):
        if index[0] == index[1] == -1:
            sets.append([aresta[0],aresta[1]])
        elif index[0] == -1:
            sets[index[1]].append(aresta[0])
        elif index[1] == -1:
            sets[index[0]].append(aresta[1])
        else:
            set1, set2 = sets[index[0]], sets[index[1]]
            sets.remove(set1)
            sets.remove(set2)
            sets.append(set1 + set2)

for s in sets:
    x, y = zip(*s)
    plt.plot(x,y,'o')
plt.show()

