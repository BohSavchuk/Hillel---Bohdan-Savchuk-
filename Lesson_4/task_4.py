n = int(input('Enter n: '))

for x in range(n):
    for y in range(1, x + 2):
        print(y, end='')
    print()