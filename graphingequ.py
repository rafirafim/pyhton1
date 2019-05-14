import matplotlib.pyplot as plt 

xval=[-1,1,2,3,4,5]
for x in xval:
    y =x**2 + 2*x + 1
    print ('x= {0} y={1}'.format(x,y))
    plt.plot(x,y,marker='o')
plt.show()