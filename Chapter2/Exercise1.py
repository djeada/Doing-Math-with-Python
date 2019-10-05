'''
Exercise 1
Using a city of your choice, find the temperature at different points of the 
day. Use the data to create two lists in your program and to create a graph
with the time of the day on the x-axis and the corresponding temperature on the
y-axis. The graph should tell you how the temperature varies with the time of 
day. Try a different city and see how the two cities compare by plotting both
lines on the same graph.
The time of day may be indicated by strings such as '10:11 AM' or '09:21 PM'
'''

import matplotlib.pyplot as plt

def plot(x,y, name):
    plt.plot(x,y, marker='+', label=name)
    plt.legend(loc='upper right')
    plt.xlabel('Time')
    plt.ylabel('Temp')

    plt.title('Time vs Temp')

    
time = ['12:00','14:00','16:00','18:00','20:00']
Warszawa = [9,10,10,9,8]
Berlin = [11,12,10,8,6]
    
plot(time,Warszawa,'Warszawa')
plot(time,Berlin,'Berlin')
plt.show()
