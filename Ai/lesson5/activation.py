import dataset
import matplotlib.pyplot as plt
import numpy as np

xs, ys = dataset.get_beans(100)

plt.title("Siz-Toxicity Functon", fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")
plt.scatter(xs, ys)

w = 0.1
b = 0.1
z = w * xs + b
a = 1 / (1 + np.exp(-z))
plt.plot(xs, a)
plt.show()
# yPre = w * xs
# plt.scatter(xs,ys)
# plt.plot(yPre,xs)
# print("修正前图像")
# plt.show()

for n in range(50000):  # 多次学习
    for i in range(100):  # 梯度下降
        x = xs[i]
        y = ys[i]
        z = w * x + b
        a = 1 / (1 + np.exp(-z))
        e = (y - a) ** 2
        alpha = 0.05
        deda = -2 * (y - a)
        dadz = a * (1 - a)
        dzdw = x
        dedw = deda * dadz * dzdw
        dzdb = 1
        dedb = deda * dadz * dzdb
        w = w - alpha * dedw
        b = b - alpha * dedb
    plt.clf()
    plt.scatter(xs, ys)
    z = w * xs + b
    a = 1 / (1 + np.exp(-z))
    plt.xlim(0, 1)
    plt.ylim(0, 1.2)
    plt.plot(xs, a)
    plt.pause(0.01)
