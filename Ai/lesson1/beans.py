import dataset
import matplotlib.pyplot as plt

xs,ys = dataset.get_beans(10)

plt.title("Siz-Toxicity Functon",fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")
plt.scatter(xs,ys)

w=0.5
yPre=0.5*xs

plt.plot(xs,yPre)

plt.show()