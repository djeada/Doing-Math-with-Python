"""
Exercise 2
Drawing the Sierpinski Triangle
Your challenge here is to write a program that draws the Sierpinski triangle
composed of a certain number of points specifid as input.
"""

import matplotlib.pyplot as plt
import random


def transformation(points):
    coefficients = [0, 0.5, 1]
    random_coeff = coefficients[random.randint(0, 2)]
    if random_coeff != 1:
        return 0.5 * points[0] + random_coeff, 0.5 * points[1] + random_coeff
    return 0.5 * points[0] + 1, 0.5 * points[1]


def draw_sierpinski(n):
    x = [0]
    y = [0]
    for i in range(n):
        temp1, temp2 = transformation((x[i], y[i]))
        x.append(temp1)
        y.append(temp2)
    return x, y


print("Enter the number of points in the triangle: ")
n = int(input())
x, y = draw_sierpinski(n)
plt.plot(x, y, "o")
plt.title("Sierpinski triangle with {0} points".format(n))
plt.show()
