'''
Exercise 1
For your challenge, imagine you've created an online questionnaire asking your
the following question: Do you play football, another sport, or no sports? Once
you have the results, create a CSV file, sports.csv, as follows:
StudentID,Football,Others
1,1,0
2,1,1
3,0,1
Create 20 such rows for the 200 students in your class. The first column is the
student ID (the survey isn't anonymous), the second colun has a 1 if the 
students has marked "football" as the sport they love to play, and the third 
column has a 1 if the student plays any other sport or none at all. Write a
program to create a Venn diagram to depict the summarized results of the survey
, as shown in Figure 5-5.
'''

import matplotlib.pyplot as plt
import matplotlib_venn as vplt
import csv

def draw_venn(sets):
    vplt.venn2(subsets=sets,set_labels =('A','B'))
    plt.show()

def read_csv(filename):
    results = []
    with open(filename) as file:
       reader = csv.reader(file,delimiter=';')
       for row in reader:
           if row[1] == '1':
               results.append((1,0))
           else:
                results.append((0,1))
    return results

results = read_csv('Survey.csv')
draw_venn([set({'A':len(results[0])}),set({'B':len(results[1])})])
