"""
Exercise 2
Implement the Gradient Descent
Your challenge is to implement a generic prgram using the gradient
descent algorithm to find the minimum value of a single-variable
function specified as input by the user. The program should also create
a graph of the function and show all the intermediate values it found
before finding the minimum.
"""

from sympy import Derivative, Symbol, sympify, solve
from sympy.core.sympify import SympifyError
import matplotlib.pyplot as plt

epsilon = 1e-6
step_size = 1e-4


def grad_descent(init_val, function, x):

    if not solve(function):
        print("Cannot continue, solution for {0}=0 does not exist".format(function))
        return None

    x_new = init_val - step_size * function.subs({x: init_val}).evalf()
    x_old = init_val

    x_traversed = []

    while abs(x_old - x_new) > epsilon:
        x_traversed.append(x_new)
        x_old = x_new
        x_new = x_old - step_size * function.subs({x: x_old}).evalf()

    return x_new, x_traversed


def frange(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start += interval

    return numbers


def create_plot(x_traversed, function, var):
    x_val = frange(-10, 10, 0.01)
    y_val = [function.subs({var: x}) for x in x_val]
    plt.plot(x_val, y_val, "black")

    y_traversed = [function.subs({var: x}) for x in x_traversed]
    plt.plot(x_traversed, y_traversed, "green")

    plt.legend(["Function", "Intermediate points"])
    plt.show()


def validate_function(function):

    try:
        return sympify(function)
    except SympifyError:
        print("Invalid function entered")
        sys.exit(1)

    return None


def main():
    function = input("Provide a function of one variable: ")
    function = validate_function(function)

    variable = input("Enter the variable to differentiate with respect to: ")
    variable = Symbol(variable)

    init_val = input("Enter the initial value of the variable: ")
    init_val = float(init_val)

    derivative = Derivative(function, variable).doit()
    var_min, x_traversed = grad_descent(init_val, derivative, variable)

    if var_min:
        print("{} : {}".format(variable.name, var_min))
        create_plot(x_traversed, function, variable)


if __name__ == "__main__":
    main()
