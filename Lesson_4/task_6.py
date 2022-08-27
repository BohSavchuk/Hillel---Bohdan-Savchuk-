
elements = [int(i) for i in input("Enter your numbers using comma: ").split(', ')]

print('NUMBERS which bigger for their neighbours: ')

for index in range(len(elements[1:-1])):
    if elements[index-1] + elements[index+1] < elements[index]:
        print('{}.{}'.format(index+1, elements[index]))