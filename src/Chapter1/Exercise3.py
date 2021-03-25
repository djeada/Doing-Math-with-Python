"""
Exercise 3
The unit conversion program we wrote in this chapter is limited to conversions
between kilometers and miles. Try extending the program to convert between
units of mass (such as kilograms and pounds) and between units of temperature
(such as Celsius and Fahrenheit).
"""


def km_to_mi(x):
    print(x, "in km is", x / 1.609, "in mil.")


def mi_to_km(x):
    print(x, "in mil is", x * 1.609, "in km.")


def c_to_f(x):
    print(x, "in Celsius is", x * (9 / 5) + 32, "in Fahrenheit.")


def f_to_c(x):
    print(x, "in Fahrenheit is", (x - 32) * (5 / 9), "in Celsius.")


def kg_to_lbs(x):
    print(x, "in kg is", x * 2.2046, "in lbs.")


def lbs_to_kg(x):
    print(x, "in lbs is", x / 2.2046, "in kg.")


x = int(input())
km_to_mi(x)
mi_to_km(x)
c_to_f(x)
f_to_c(x)
kg_to_lbs(x)
lbs_to_kg(x)
