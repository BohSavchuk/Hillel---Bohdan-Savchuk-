x = int(input('Put x: '))
y = int(input('Put y: '))
c = 1
while x < y:
    x = x * 1.1
    c = c + 1
print(abs(c))