'''
Exercise 1
Verify the Continuity of a Function at a Point
Your challenge here is to write a program that will (1) accept a single-
variable function and a value as inputs and (2) check whether the input
function is continuous at the point where the variable assumes the value
input.
'''

from sympy import Limit, Symbol, sympify
from sympy.core.sympify import SympifyError

def isContinous(point, function, symbol):
	right_lim = Limit(function, symbol, point).doit()
	left_lim = Limit(function, symbol, point, dir='-').doit()
	
	if function.subs({symbol:point}) == left_lim == right_lim:
		return True
	return False

print('Enter a function in one variable: ')
function = input()

print('Enter the variable to differentiate with respect to: ')
symbol = input()

print('Enter the initial value of the variable: ')
initialValue = float(input())

try:
    function = sympify(function)
    
except SympifyError:
    print('Invalid function entered')

else:
    symbol = Symbol(symbol)    
    if isContinous(initialValue, function , symbol):
        print('{0} is continuous at {1}'.format(function , initialValue))
    else:
        print('{0} is not continuous at {1}'.format(function , initialValue))
