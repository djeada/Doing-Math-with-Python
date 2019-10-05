'''
Exercise 3
Your challenge here is to enhance the trajectory comparison program in a few
ways. First, your program should print the time of flight, maximum horizontal
distance, and maximum vertical distance traveled for each of the velocity and
angle of projection values, supplied by the user. For example, here's how the
program should ask the user for inputs:
    
How many trajectories? 3
Enter the initial velocity for trajectory 1 (m/s): 45
Enter the angle of projection for trajectory 1 (degrees): 45 
Enter the initial velocity for trajectory 1 (m/s): 60
Enter the angle of projection for trajectory 1 (degrees): 45
Enter the initial velocity for trajectory 1 (m/s): 45
Enter the angle of projection for trajectory 1 (degrees): 90
Your program should also ensure the erroneous input is properly handled using a
try. . . except block, just as in the original program.

'''

import matplotlib.pyplot as plt
import math

g = 9.81

def plot(x, y, name):
    plt.plot(x, y, label=name)
    plt.legend(loc='upper right')
    plt.xlabel('Range [m]')
    plt.ylabel('Hegiht [m]')
    plt.title('Projectile motion')

def trajectory(u, theta, i):
    
    theta = math.radians(theta)

    print(u*math.sin(theta)*2*u*math.sin(theta)/g-0.5*g*(2*u*math.sin(theta)/g)**2)
    time = (2*u*math.sin(theta)/g)

    x = [u*math.cos(theta)*t for t in range(0,int(time*1000))]
    y = [(abs(u*math.sin(theta)*t-g*t**2/2000))/1000 for t in range(0,int(time*1000))]

    print('Total time in secs : ', time) 
    print('Total range in m: ', max(x))
    print('Maximum hegiht in m: ', max(y))

    plot(x, y, 'projectile ' + str(i+1))
    
num = int(input('How many trajectories? '))
for i in range(num):
    try:
        u = int(input('Enter the initial veolcity (m/s): '))
        theta = 0
        while not (theta > 0 and theta < 90):
            theta = int(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You enter an invalid input')
    else:
        trajectory(u, theta, i)

plt.show()
