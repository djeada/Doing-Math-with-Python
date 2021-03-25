"""
Exercise 3
Your challenge is to write a program that's capable of finding the sum of an
arbitrary series when you supply the nth term of the series and the number of 
terms in it. Here's and example of how the program would work:
Enter the nth term: a+(n-1)*d
Enter the number of terms: 3
3a + 3d
In this example, the nth term supplied is that of an arithmetic progression. 
Starting with a and d as the common difference, the number of terms up to a 
which the sum is to be calculated is 3. The sum turns out the be 3a + 3d, which 
agrees with the known formula for the same.
"""
from sympy import expand, summation, sympify, Symbol
from sympy.core.sympify import SympifyError

expr = input("Enter the nth term: ")

try:
    expr = sympify(expr)
except SympifyError:
    print("Invalid input")

terms = input("Enter the number of terms: ")

print(expand(summation(expr, (Symbol("n"), 1, terms))))
