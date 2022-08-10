x = int(input('Please enter your number:'))

c = x % 10
b = x % 100 // 10
a = x // 100

print(a + b + c)