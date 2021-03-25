"""
Exercise 1
Packing Circles into a Square
In this challenge, you'll attempt a very simplified version of the "circles 
packed into a square" problem. How many circles of radius 0.5 will fit in the 
square preoduced by this code?
def draw_square():
    ax = plt.axes(xlim= (0,6), ylim = (0,6))
    square = plt.Polygon([(1,1), (5,1), (5,5), (1,5)], fc='b',closed = False)
    ax.add_patch(square)
    plt.show()
"""

import matplotlib.pyplot as plt


def draw_square():
    return plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], fc="b", closed=False)


def draw_circle(x, y):
    return plt.Circle((x, y), radius=0.5)


def draw_shapes():
    ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
    ax.add_patch(draw_square())

    for y in range(1, 5):
        for x in range(1, 5):
            ax.add_patch(draw_circle(x + 0.5, y + 0.5))
    plt.show()


draw_shapes()
