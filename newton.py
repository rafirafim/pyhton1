import matplotlib.pyplot as plt
# draw graph
def draw(x,y):
    plt.xlabel('Distance between the objects')
    plt.xlabel('Distance between the objects')
    plt.grid(True)
    plt.plot(x,y,marker='*')
    plt.show()
     
def force_r():
    r=range(100,1001,50)
    f=[]
    m1=float(input('Enter the mass of the first object : '))
    m2=float(input('Enter the mass of the second object : '))
    g=6.64*(10**(-11))
    for dis in r:
        x=g*(m1*m2)/(dis**2)
        f.append(x)
    draw(r,f)
force_r()
