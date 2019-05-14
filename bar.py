import matplotlib.pyplot as plt 
def creat_bar_cart(data,label):
    num_bars=len(data)
    positions=range(1,num_bars+1)
    plt.barh(positions,data,align='center')
    plt.yticks(positions,label)
    plt.grid()
    plt.show()

steps=[6543,5682,7300,8759,1530,9800,1150]
labels=['sun','mon','tue','wed','thu','fri','sat']
creat_bar_cart(steps,labels)