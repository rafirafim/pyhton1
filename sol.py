def root(a,b,c):
    d = (b**2-4*a*c)**0.5
    s_1=(-b+d)/(2*a)
    s_2=(-b-d)/(2*a)

    print('Solution 1 : {0}'.format(s_1))
    print('Solution 2 : {0}'.format(s_2))

print(' The equation is of the form ax^2 + bx + c')
a = input('Eneter the value of a :')
b = input('Eneter the value of b :')
c = input('Eneter the value of c :')
root(float(a),float(b),float(c))