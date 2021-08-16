import dataset
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
xs,ys = dataset.get_beans(100)

plt.title("Siz-Toxicity Functon", fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")
plt.xlim(0, 1)
plt.ylim(0, 1.5)
plt.scatter(xs, ys)

w = 0.1
b = 0.1
yPre= w*xs
plt.plot(xs,yPre)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.set_zlim(0,2)

ws = np.arange(-1, 2, 0.1)

bs = np.arange(-2,2,0.01)
for b in bs:
    es = []
    for w in ws:
        yPre = w*xs+b
        e = np.sum((ys-yPre)**2)*(1/100)
        es.append(e)
    #plt.plot(ws, es)
    ax.plot(ws, es, b, zdir='y')

plt.show()