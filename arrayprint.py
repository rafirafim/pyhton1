nMax = int(input('Enter the number of elements in the array : '))
n = 1
a = []
while n < nMax+1:
    c =float(input('Enter the number :'))
    a.append(c)
    c=0
    n = n +1
print(a)
print(' ')
for i in range(0,nMax):
    print(a[i])