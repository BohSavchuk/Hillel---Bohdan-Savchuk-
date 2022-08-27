v = int(input('Please enter your speed:'))
t = int(input('Please enter your time:'))
s = int(v * abs(t))
if v > 0 and s <= 100:
    print('You are already completed', s, 'km.', 'Keep it up')
elif v < 0 and s <= 100:
    100 - (s * -1)
    print('You are already completed', abs(s), 'km.', 'Hurry up')
else:
    print('Congratulations! You are already finished 100km')
