import array
import matplotlib.pyplot as plt
import numpy as np
import random

def plotColor(x, y, color):
    plt.plot(x, y, color=color)
    plt.fill_between(x, y, color=color, alpha=0.3)

def plotRandomColor(x, y, c):
    colors = ['red', 'green', 'blue', 'springgreen', 'turquoise', 'goldenrod', 'magenta', 'dodgerblue', 'crimson', 'purple', 'cyan']
    color = random.choice(colors)
    plt.plot(x, y, color=color)
    plt.fill_between(x, y, color=color, alpha=0.3)

def whale():
    x = np.arange(0, 9, 0.1)
    y = 2/27.0*x**2-3
    plotRandomColor(x, y, "#E1D7EB")

    x = np.arange(-10, 0, 0.1)
    y = 0.04*x**2-3
    plotRandomColor(x, y, "#E2D4EB")

    x = np.arange(-9, -3, 0.1)
    y = 2/9*((x + 6)**2)+1
    plotRandomColor(x, y, "#E5CFEB")

    x = np.arange(-3, 9, 0.1)
    y = -1/12*(x-3)**2+6
    plotRandomColor(x, y, "#E9C6EA")

    x = np.arange(5, 8.3, 0.1)
    y = 1/9*(x-5)**2+2
    plotRandomColor(x, y, "#F4AFE9")

    x = np.arange(5, 8.5, 0.1)
    y = 1/8*(x-7)**2+1.5
    plotRandomColor(x, y, "#E6A7EB")

    x = np.arange(-13, -9, 0.1)
    y = -0.75*(x+11)**2+6
    plotRandomColor(x, y, "#D69EED")

    x = np.arange(-15, -13, 0.1)
    y = -0.5*(x+13)**2+3
    plotRandomColor(x, y, "#C393EF")

    x = np.arange(-15, -10, 0.1)
    y = [1] * len(x) 
    plotRandomColor(x, y, "#B98DF0")

    x = np.arange(3, 4, 0.1)
    y = [3] * len(x)
    plotRandomColor(x, y, "#AF88F1")

def parabola():
    x = np.arange(0, 10, 1)
    y = x**2-5*x+6

    plt.plot(x, y, color='blue', marker='D', markersize=4, label="x**2*5x+6")

def test():
    x = [1, 2, 3, 4]
    y = [2, 4, 8, 16]

    plt.plot(x, y, linestyle='-', marker='o', color='#FFAA00',
             markersize=4, markerfacecolor='lightblue', label="Tõusev joon")
    plt.plot(y, x, linestyle='--', marker='x', color='green',
             markersize=4, label="Laskuv joon")


whale()

plt.title("Lihtne graafik")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()


