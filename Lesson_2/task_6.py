tuple_1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

#Check if element x is present
x = float(input('Enter x:'))

if x in tuple_1:
    print(x, 'X is in the following list ', tuple_1)
else:
    print(x, 'is not in the following list', tuple_1)
