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
pts = [
        [-7.627792, -5.765306],
        [-6.754342, 4.438776],
        [-3.617866, 0.969388],
        [-3.300248, -7.44898],
        [-2.942928, -2.091837],
        [-1.473945, 6.22449],
        [-0.918114, -5.05102],
        [-0.719603, 0.765306],
        [-0.203474, 4.336735],
        [0.947891, -1.581633],
        [2.059553, 2.5],
        [3.369727, 6.581633],
        [4.124069, -3.72449],
        [4.441687, 4.387755],
        [4.878412, 1.122449],
        [6.307692, -8.77551],
        [6.665012, 5.459184],
        [7.141439, -1.938776],
        [8.054591, -6.326531]
        ]

arestas = [
        [ pts[0], pts[1] ],
        [ pts[0], pts[2] ],
        [ pts[0], pts[3] ],
        [ pts[0], pts[4] ],
        [ pts[1], pts[2] ],
        [ pts[1], pts[5] ],
        [ pts[2], pts[4] ],
        [ pts[2], pts[5] ],
        [ pts[2], pts[7] ],
        [ pts[2], pts[8] ],
        [ pts[3], pts[4] ],
        [ pts[3], pts[6] ],
        [ pts[3], pts[15] ],
        [ pts[4], pts[6] ],
        [ pts[4], pts[7] ],
        [ pts[5], pts[8] ],
        [ pts[5], pts[11] ],
        [ pts[6], pts[7] ],
        [ pts[6], pts[9] ],
        [ pts[6], pts[12] ],
        [ pts[6], pts[15] ],
        [ pts[7], pts[8] ],
        [ pts[7], pts[9] ],
        [ pts[7], pts[10] ],
        [ pts[8], pts[10] ],
        [ pts[8], pts[11] ],
        [ pts[9], pts[10] ],
        [ pts[9], pts[12] ],
        [ pts[10], pts[11] ],
        [ pts[10], pts[12] ],
        [ pts[10], pts[13] ],
        [ pts[10], pts[14] ],
        [ pts[11], pts[13] ],
        [ pts[11], pts[16] ],
        [ pts[12], pts[14] ],
        [ pts[12], pts[15] ],
        [ pts[12], pts[17] ],
        [ pts[12], pts[18] ],
        [ pts[13], pts[14] ],
        [ pts[13], pts[16] ],
        [ pts[14], pts[16] ],
        [ pts[14], pts[17] ],
        [ pts[15], pts[18] ],
        [ pts[16], pts[18] ],
        [ pts[16], pts[17] ],
        [ pts[17], pts[18] ],
    ]

dPts = {}
for pt in pts:
    dPts.update(
        {
            hashlist(pt): {
                "pt":pt,
                "arestas": []
            }
        })

for aresta in arestas:
    dPts[hashlist(aresta[0])]["arestas"].append(aresta[1])
    dPts[hashlist(aresta[1])]["arestas"].append(aresta[0])

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

