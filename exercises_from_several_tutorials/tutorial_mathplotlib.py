import matplotlib.pyplot as plt
import numpy as np
from math import pi

def winkelfunktionen():
    # Prepared Data
    x = np.linspace(0,2*pi, 100)

    y = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)

    f, ax = plt.subplots()
    xmin, xmax, ymin, ymax = 0, 6, -1, 1
    plt.axis([xmin, xmax, ymin, ymax])

    ax.plot(x, y)
    ax.plot(x, y2)
    ax.plot(x, y3)
    plt.show()

def temperaturgraph():
    days = list(range(1, 9))
    celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
    plt.xlabel('Day')
    plt.ylabel('Degrees Celsius')
    plt.plot(days, celsius_min, "y",
             days, celsius_min, "oy",
             days, celsius_max, "r",
             days, celsius_max, "or")
    print("The current limits for the axes are:")
    print(plt.axis())
    print("We set the axes to the following values:")
    xmin, xmax, ymin, ymax = 0, 10, 0, 45
    print(xmin, xmax, ymin, ymax)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()


if __name__ == '__main__':
    winkelfunktionen()
    #temperaturgraph()