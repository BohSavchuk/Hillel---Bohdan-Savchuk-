a = int(input('Число А: '))
b = int(input('Число B: '))
if (a < b):
 for i in range(a, b + 1, 1):
   print(i, end=" ")
else:
 for i in range(a, b - 1, -1):
   print(i, end=" ")
