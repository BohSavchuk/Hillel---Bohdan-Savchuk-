n = int(input('Please enter your number: '))
factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(f'Your factorial is {factorial}')