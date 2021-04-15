"""
Exercise 3
Find the area enclosed by two curves between two points.
"""

from sympy import Integral, Symbol, SympifyError, sympify


def find_area(f1x, f2x, var, a, b):
    return Integral(f1x - f2x, (var, a, b)).doit()


def validate_function(function):

    try:
        return sympify(function)
    except SympifyError:
        print("Invalid function entered")
        sys.exit(1)

    return None


if __name__ == "__main__":
    f1 = input("Enter the upper function in one variable: ")
    f1 = validate_function(f1)

    f2 = input("Enter the lower upper function in one variable: ")
    f2 = validate_function(f2)

    variable = input("Enter the variable: ")
    variable = Symbol(variable)

    lower_bound = float(input("Enter the lower bound of the enclosed region: "))
    upper_bound = float(input("Enter the upper bound of the enclosed region: "))

    print(
        "Area enclosed by {} and {} is {} ".format(
            f1, f2, find_area(f1, f2, variable, lower_bound, upper_bound)
        )
    )
