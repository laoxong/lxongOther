import dataset
import matplotlib.pyplot as plt

xs,ys = dataset.get_beans(100)

plt.title("Siz-Toxicity Functon",fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")
plt.scatter(xs,ys)

w=0.5
for m in range(100):
    for i in range(100):
        x = xs[i]
        y=ys[i]
        yPre = w*x
        e = y - yPre
        alpha = 0.05
        w = w + alpha*e*x

yPre = w * xs

plt.plot(xs,yPre)

plt.show()