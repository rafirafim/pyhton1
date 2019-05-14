from numpy import *
from numpy.linalg import inv,solve
A =[[1,2,3],[4,5,6],[7,8,9]]
B =[[1,0,2],[0,1,0],[0,0,1]]
print ('Diagonal A is')
print(diagonal(A))
print ('Diagonal B is')
print(diagonal(B))
print ('trace A is')
print(trace(A))
print ('trace B is')
print(trace(B))
print('dot product')
print(dot(A,B))
print('Inner')
print(inner(A,B))
z=inv(A)
print z
