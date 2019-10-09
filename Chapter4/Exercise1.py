'''
Exercise 1
Write a program that will ask the user to input an expression, calculate its
factors, and print them. Your program should be able to handle invalid input
by making use of exception handling.
'''

    
from sympy import factor, sympify, pprint
from sympy.core.sympify import SympifyError

while True:
    expression = input('Enter expression: ')

    try:
        print(factor(sympify(expression)))
        break
    except SympifyError:
        print('Invalid expression')

