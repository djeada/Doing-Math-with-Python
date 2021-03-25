"""
Exercise 2
Implement the Gradient Descent
Your challenge is to implement a generic prgram using the gradient
descent algorithm to find the minimum value of a single-variable
function specified as input by the user. The program should also create
a graph of the function and show all the intermediate values it found
befire finding the minimum.
"""

from sympy import Derivative, Symbol, sympify
from sympy.core.sympify import SympifyError

epsilon = 1e-6


def grad_descent(initialValue, derivative, symbol):
    i = 1e-4
    x_old = initialValue
    x_new = x_old - i * derivative.subs({symbol: x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old - i * derivative.subs({symbol: x_old}).evalf()

    return x_new


print("Enter a function in one variable: ")
function = input()

print("Enter the variable to differentiate with respect to: ")
symbol = input()

print("Enter the initial value of the variable: ")
initialValue = float(input())

try:
    function = sympify(function)
except SympifyError:
    print("Invalid function entered")
else:
    symbol = Symbol(symbol)
    d = Derivative(function, symbol).doit()

    var_min = grad_descent(initialValue, d, symbol)
    print("{0}: {1}".format(symbol.name, var_min))
    print("Minimum value: {0}".format(function.subs({symbol: var_min})))
