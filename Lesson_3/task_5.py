import random
guesses = 0
random_number = random.randint(1, 10)

while guesses < 3:
    guess = int(input("Please enter number from 1 to 10:"))
    guesses += 1
    if guess != random and guesses < 3:
        print('Wrong, try one more time')
    if guess == random:
        break

if guess == random_number:
    print('You won')
else:
    print('You lost, the correct number is {0}'.format(random_number))

