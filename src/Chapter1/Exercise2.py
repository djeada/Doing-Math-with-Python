"""
Exercise 2
Our multiplication table generator is cool, but it prints only the first
10 multiples. Enhance the generator so that the user can specify both the
number and up to which multiple. For example, I should be able to input that
I want to see a table listing the first 15 multiples of 9.
"""


def mult(x, end):
    for i in range(x, x * (end + 1), x):
        print("number: ", x, " mult by ", int(i / x), " is ", i)


x = int(input("Enter a number: "))
y = int(input("Enter the last multiple: "))

mult(x, y)
