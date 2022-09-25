#First cell
a = int(input('Enter x for 1st cell:'))
b = int(input('Enter y for 1st cell:'))

#Seconf cell
aa = int(input('Enter x for 2nd cell:'))
bb = int(input('Enter y for 2nd cell:'))

#Formula
x = abs(a - aa)
y = abs(b - bb)
if x == 1 and y == 2 or x == 2 and y == 1:
    print('YES')
else:
    print('NO')


    print( )