"""
Exercise4
Find the length of a curve between two points
"""

from sympy import Derivative, Integral, Symbol, sqrt, SympifyError, sympify


def find_length(fx, var, a, b):
    deriv = Derivative(fx, var).doit()
    return Integral(sqrt(1 + deriv ** 2), (var, a, b)).doit().evalf()


def validate_function(function):

    try:
        return sympify(function)
    except SympifyError:
        print("Invalid function entered")
        sys.exit(1)

    return None


if __name__ == "__main__":
    function = input("Provide a function of one variable: ")
    function = validate_function(function)

    variable = input("Enter the variable to differentiate with respect to: ")
    variable = Symbol(variable)

    lower_bound = float(input("Enter the lower limit of the variable: "))
    upper_bound = float(input("Enter the upper limit of the variable: "))

    print(
        "Length of {} between {} and {} is {} ".format(
            function,
            lower_bound,
            upper_bound,
            find_length(function, variable, lower_bound, upper_bound),
        )
    )
