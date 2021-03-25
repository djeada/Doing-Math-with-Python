"""
Exercise 4
For this challenge, create a function, isolve(), that will take any inequality, 
solve it, and then return the solution.
"""
from sympy import sympify, solveset, S, Symbol
from sympy.core.sympify import SympifyError

expr = input("Enter your inequality ")

try:
    expr = sympify(expr)
except SympifyError:
    print("Invalid input")


def issolve(expr):
    return solveset(expr, Symbol("x"), S.Reals)


print(issolve(expr))
