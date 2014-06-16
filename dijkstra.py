#-*- coding:utf8 -*-
from numpy import *
from numpy.random import *
from matplotlib import pyplot as plt

def hashlist(l):
    return ','.join([str(i) for i in l])

def distancia(pt1,pt2):
    soma = 0
    for i in range(len(pt1)):
        soma += pow(pt2[i]-pt1[i],2)
    return sqrt(soma)

#Gera lista de pontos em uma estrutura de lista de pontos(para plotagem), lista de arestas (para plotagem) e grafo num dicionário(para o dijkstra em si)
pts = (randn(5,2)*5).tolist()
pts += (randn(5,2)*5+asarray([10,10])).tolist()
pts += (randn(5,2)*5+asarray([-10,10])).tolist()
pts += (randn(5,2)*5+asarray([10,-10])).tolist()
pts += (randn(5,2)*5+asarray([-10,-10])).tolist()

dPts = {}
for pt in pts:
    dPts.update(
        {
            hashlist(pt): {
                "pt":pt,
                "arestas": []
            }
        })

arestas = []
for pt in pts:
    for l in range(randint(2)+1):
        sel = pt
        while sel == pt:
            sel = pts[randint(len(pts))]
        if not ([pt,sel] in arestas or [sel,pt] in arestas):
            arestas.append([pt,sel])
            dPts[hashlist(pt)]["arestas"].append(sel)
            dPts[hashlist(sel)]["arestas"].append(pt)

#Seleciona nó inicial e final, garantindo serem diferentes
start = hashlist(pts[randint(len(pts))])
end = hashlist(pts[randint(len(pts))])
while end == start:
    end = hashlist(pts[randint(len(pts))])


#Desenha grafo e nós inicial e final
for aresta in arestas:
    x,y = zip(*aresta)
    plt.plot(x,y,'g')

x, y = zip(*pts)
plt.plot(x,y,'bo')
x, y = dPts[start]["pt"]
plt.plot(x,y,'ro')
x, y = dPts[end]["pt"]
plt.plot(x,y,'ko')
plt.show()

############
# Dijkstra #
############

#Calcula-se as menores distâncias para cada nodo
dists = {}
for k in dPts.keys():
    dists[k] = [float("inf"), None]

dists[start] = [0, start]
current = start
visited = []
while current != None:
    for pt in dPts[current]["arestas"]:
        d = distancia(pt, dPts[current]["pt"]) + dists[current][0]
        if d < dists[hashlist(pt)][0]:
            dists[hashlist(pt)] = [d,current]

    visited.append(current)
    current = None
    for k in sorted(dists, key = lambda k: dists[k][0]):
        if not k in visited:
            current = k
            break

#Reconstrói o caminho do nodo final até o inicial
path = []
if dists[end][1] != None:
    path.append(end)
    while path[-1] != start:
        path.append(dists[path[-1]][1])
else:
    print "Start e end estão em conjuntos independentes"




#Desenha grafo em segundo plano
for aresta in arestas:
    x,y = zip(*aresta)
    plt.plot(x,y,'c')
x, y = zip(*pts)
plt.plot(x,y,'wo')

#Desenha path selecionado
if path != []:
    for i in range(len(path)-1):
        x,y = zip(*[dPts[pt]["pt"] for pt in path[i:i+2]])
        plt.plot(x,y,'g')
    x,y = zip(*[dPts[pt]["pt"] for pt in path])
    plt.plot(x,y,'yo')

#Desenha pontos iniciais e finais
x, y = dPts[start]["pt"]
plt.plot(x,y,'ro')
x, y = dPts[end]["pt"]
plt.plot(x,y,'ko')
plt.show()

