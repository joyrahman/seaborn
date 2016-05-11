import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.1);
print x
y = np.sin(x)
print y
plt.plot(x,y)
#plt.show()



def plot_slope(X, Y):
    Xs = X[1:] - X[:-1]
    Ys = Y[1:] - Y[:-1]
    plt.plot(X[1:], Ys / Xs)

X = np.linspace(-3, 3, 100)
Y = np.exp(-X ** 2)
plt.plot(X, Y)
plot_slope(X, Y)
plt.show()