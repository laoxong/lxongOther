import dataset
import matplotlib.pyplot as plt
import numpy as np

xs, ys = dataset.get_beans(100)

w = 0.1

plt.title("Siz-Toxicity Functon", fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")

yPre = w * xs
plt.scatter(xs, ys)
plt.plot(xs, yPre)
print("修正前图像")

plt.show()

es = (ys - yPre) ** 2
sum_e = np.sum(es)
sum_e = (1 / 100) * sum_e
ws = np.arange(0, 3, 0.1)

es = []
for w in ws:
    yPre = w * xs
    e = (1 / 100) * np.sum((ys - yPre) ** 2)
    es.append(e)
plt.plot(ws, es)
plt.title("Cost Function", fontsize=12)
plt.xlabel("w")
plt.ylabel("e")
print("代价函数")
plt.show()

wMin = np.sum(xs * ys) / np.sum(xs * xs)
print("最小点w:" + str(wMin))

yPre = wMin * ws
plt.plot(ws, yPre)
plt.scatter(xs, ys)
plt.title("Siz-Toxicity Functon After", fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")
print("修正后图像")
plt.show()
