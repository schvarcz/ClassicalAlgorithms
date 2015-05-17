from numpy import *
from matplotlib import pyplot as plt
from numpy.linalg import solve

def ransac(pts, model, iterations=100, sampleSize=3, threshold = 1.4, minInliers = 28):
    maxInliers = 0
    bestParams, bestInliers = None, None
    ptsA = asarray(pts)
    for i in range(iterations):
        random_selection = (random.random_sample(3)*len(pts)).astype(int)
        params = model.model(ptsA[random_selection].tolist())
        if params == None:
            continue
        inliers, outliers = model.fit(pts, params, threshold)
        
        if len(inliers) > maxInliers:
            maxInliers = len(inliers)
            bestInliers = inliers
            bestParams = params
        
        if maxInliers >= minInliers:
            break
    
    params = model.model(bestInliers)
    inliers, outliers = model.fit(pts, params, threshold)
    return params, inliers, outliers
    
class LSE(object):

    def model(self, pts):
        x, y = zip(*pts)
        x, y = asarray(x), asarray(y)
        A = matrix([x**3,x**2,x,ones(x.shape)]).T
        b = matrix(y).T
        params = solve(A.T*A,A.T*b).A1
        #print "A = {0} B = {1} C = {2} D = {3}".format(params[0], params[1], params[2], params[3])
        return params
    
    
    def fit(self, pts, params, threshold):
        x, y = zip(*pts)
        x, y = asarray(x), asarray(y)
        erros = y - (params[0]*x**3+params[1]*x**2+params[2]*x+params[3])
        inliers, outliers = [], []
        for idx in range(len(erros)):
            erro = erros[idx]
            if abs(erro) < threshold:
                inliers.append(pts[idx])
            else:
                outliers.append(pts[idx])
        #print "erros: ", erros
        return inliers, outliers
    
    
    def fixLine(self, pts, params):
        x, y = zip(*pts)
        x, y = asarray(x), asarray(y)
        y = params[0]*x**3+params[1]*x**2+params[2]*x+params[3]
        return zip(x,y)

pts = [
    [ 0 , -445.267302865 ],
    [ 1 , -100.003592336 ],
    [ 2 , -297.050598923 ],
    [ 3 , -111.414221236 ],
    [ 4 , 941.825076237 ],
    [ 5 , -321.34525499 ],
    [ 6 , 438.482637526 ],
    [ 7 , -702.706451548 ],
    [ 8 , -341.783632207 ],
    [ 9 , 612.997082795 ],
    [ 10 , 441.313244946 ],
    [ 11 , 532.955583181 ],
    [ 12 , -442.040207288 ],
    [ 13 , 771.211974348 ],
    [ 14 , 648.917795481 ],
    [ 15 , 336.764539538 ],
    [ 16 , 767.525485044 ],
    [ 17 , -894.718013378 ],
    [ 18 , 421.009523594 ],
    [ 19 , 867.951457584 ],
    [ 20 , -11.5334207505 ],
    [ 21 , 1237.74961439 ],
    [ 22 , -93.0346884437 ],
    [ 23 , 775.103644994 ],
    [ 24 , 1075.50394509 ],
    [ 25 , -148.249684919 ],
    [ 26 , 1013.56552909 ],
    [ 27 , 639.356105195 ],
    [ 28 , 1449.69550958 ],
    [ 29 , 780.910674168 ],
    [ 30 , 826.37799663 ],
    [ 31 , 1319.91181648 ],
    [ 32 , 1183.11322 ],
    [ 33 , 1575.05565735 ],
    [ 34 , 371.917868799 ],
    [ 35 , 1869.38014792 ],
    [ 36 , 961.872044281 ],
    [ 37 , 1599.23556361 ],
    [ 38 , 1083.17328461 ],
    [ 39 , 2193.58228314 ],
    [ 40 , 1953.14855119 ],
    [ 41 , 2103.00076541 ],
    [ 42 , 2550.27032003 ],
    [ 43 , 1392.59207363 ],
    [ 44 , 2344.14293519 ],
    [ 45 , 2306.54716779 ],
    [ 46 , 2235.929142 ],
    [ 47 , 2564.01764847 ],
    [ 48 , 2325.22137544 ],
    [ 49 , 2691.19966432 ],
    [ 50 , 3227.4397964 ],
    [ 51 , 2226.89151462 ],
    [ 52 , 2510.83469783 ],
    [ 53 , 2747.43731226 ],
    [ 54 , 2098.93980048 ],
    [ 55 , 3123.97023786 ],
    [ 56 , 3257.28757952 ],
    [ 57 , 3150.87113505 ],
    [ 58 , 3578.51273722 ],
    [ 59 , 3085.86862447 ],
    [ 60 , 4321.62325808 ],
    [ 61 , 4491.41985395 ],
    [ 62 , 3792.53850562 ],
    [ 63 , 3360.3285873 ],
    [ 64 , 4065.37726169 ],
    [ 65 , 3899.47192729 ],
    [ 66 , 5130.21869209 ],
    [ 67 , 4710.64870619 ],
    [ 68 , 4356.36506042 ],
    [ 69 , 5223.03245095 ],
    [ 70 , 4549.51439295 ],
    [ 71 , 5390.51094568 ],
    [ 72 , 6026.65848251 ],
    [ 73 , 4539.22421737 ],
    [ 74 , 5018.27577085 ],
    [ 75 , 5487.32862174 ],
    [ 76 , 6545.73485707 ],
    [ 77 , 5832.87366622 ],
    [ 78 , 5672.22241403 ],
    [ 79 , 6344.11705429 ],
    [ 80 , 6891.56831752 ],
    [ 81 , 6268.97131779 ],
    [ 82 , 6678.228422 ],
    [ 83 , 7250.13475912 ],
    [ 84 , 7278.91216909 ],
    [ 85 , 6873.24595323 ],
    [ 86 , 7636.97699997 ],
    [ 87 , 7659.83934359 ],
    [ 88 , 7068.84868161 ],
    [ 89 , 8554.74555516 ],
    [ 90 , 8113.68680936 ],
    [ 91 , 8479.56964217 ],
    [ 92 , 8856.79691885 ],
    [ 93 , 9406.90128541 ],
    [ 94 , 9368.47796499 ],
    [ 95 , 8902.93120658 ],
    [ 96 , 9492.40077676 ],
    [ 97 , 9648.48946518 ],
    [ 98 , 8582.89427901 ],
    [ 99 , 9509.88587441 ],
]
x,y_e = zip(*pts)
x, y_e = asarray(x), asarray(y_e)
#x =arange(100)
y= x**2 + x*2 + 10
#y_e = y + random.randn(len(x))*500

#for i in range(100):
#    print "[", x[i],"," , y_e[i], "],"
    
#for i in range(100):
#    print "pts.at<float>(1, ",x[i],") =" , y_e[i], ";"
line = zip(x,y_e)


l = LSE()
params, inliers, outliers = ransac(pts, l, threshold = 500)
#params = l.model(line)
#inliers, outliers = l.fit(line,params,500)

#print len(inliers), len(outliers)
linefixed = l.fixLine(line,params)
print linefixed

_,y_f = zip(*linefixed)

plt.plot(x,y)
plt.plot(x,y_e, "b+")
plt.plot(x,y_f)

if inliers != []:
    x_i,y_i = zip(*inliers)
    plt.plot(x_i,y_i, "g+")

if outliers != []:
    x_o,y_o = zip(*outliers)
    plt.plot(x_o    ,y_o, "r+")

plt.show()

