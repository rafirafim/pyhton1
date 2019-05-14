nMax = float(input('Enter the number of elements in the array : '))
n = 1
a = []
while n < nMax:
    c =float(input('Enter the number :'))
    a.append(c)
    c=0
    n = n +1
print(a)
for index,item in enumerate(a):
    print index,item