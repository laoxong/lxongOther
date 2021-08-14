import dataset
import matplotlib.pyplot as plt
import numpy as np

xs,ys = dataset.get_beans(100)

plt.title("Siz-Toxicity Functon",fontsize=12)
plt.xlabel("Size")
plt.ylabel("Toxicity")

w = 0.1
#yPre = w * xs
#plt.scatter(xs,ys)
#plt.plot(yPre,xs)
#print("修正前图像")
#plt.show()
for n in range(50):#多次学习
    for i in range(100):#梯度下降
        x = xs[i]
        y =ys[i]
        #k = 2aw + b
        #a=x^2 b=-2xy
        k = 2*(x**2)*w+(-2*x*y)
        alpha = 0.1 #学习率
        w = w - alpha * k
        plt.clf() #清空图像
        yPre = w * xs
        plt.scatter(xs, ys)
        plt.plot(xs, yPre)
        plt.xlim(0,1)
        plt.ylim(0,1.2)
        plt.pause(0.01)
'''
yPre = w * xs
plt.scatter(xs,ys)
plt.plot(xs,yPre)
print("修正后(梯度下降)图像")
plt.show()
'''