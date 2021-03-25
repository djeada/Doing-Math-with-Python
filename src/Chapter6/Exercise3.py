"""
Exercise 3
Exploring Henon's Function
Your challenge here is to write a program to create a graph showing  
iteractions of this transformation, starting with the point (1,1).
"""

import matplotlib.pyplot as plt


def transformation(points):
    return points[1] + 1 - 1.4 * points[0] ** 2, 0.3 * points[0]


def draw_henon(n):
    x = [1]
    y = [1]
    for i in range(n):
        temp1, temp2 = transformation((x[i], y[i]))
        x.append(temp1)
        y.append(temp2)
    return x, y


x, y = draw_henon(20000)
plt.plot(x, y, "o")
plt.title("Henon's functions with 20,000 points")
plt.show()
