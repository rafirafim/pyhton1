import matplotlib.pyplot as plt 
import math

def drw(x,y):
    
    plt.plot(x,y)
    plt.show()
    print('sdfs')
    

def frange(start,final,interval):
    number=[]
    while start<final:
        number.append(start)
        start=start+interval
    return number

def graph(u,theta):
    theta=math.radians(theta)
    g = 9.8
    time=2*u*math.sin(theta)/g
    intervals=frange(0,time,0.001)
    x =[]
    y =[]
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    drw(x,y)
    try:
        u = float(input('Enter the initial velocity (m/s) :'))
        theta = float(input('\Enter the angle of projection (degrees:'))
    except ValueERROR:
        PRINT('You entered an invalid input. ')
    else:
        graph(u,theta)
        print('hghgf')


