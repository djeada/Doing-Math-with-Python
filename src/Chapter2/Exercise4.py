"""
Exercise 4
For this challenge, you'll write a program that creates a bar chart for easy 
comparison of weekly expenditures. The program should first ask for the number
of categories for the expenditures and the weekly total expenditure in each
category, and then it should create the bar chart showing these expenditures.

"""

import matplotlib.pyplot as plt
import numpy as np


def bar_chart(categories, expenditures):

    index = np.arange(len(categories))
    plt.bar(index, expenditures)
    plt.ylabel("Expenditure")
    plt.ylim([0, max(expenditures) + 1])
    plt.xticks(index, categories, fontsize=15, rotation=30)
    plt.xlabel("Category")
    plt.title("Weekly Expenditures")
    plt.grid()


num = int(input("Enter the number of categories: "))

categories = []
expenditures = []

for i in range(num):
    categories.append(input("Category: "))
    expenditures.append(int(input("Expenditure: ")))

bar_chart(categories, expenditures)

plt.show()
