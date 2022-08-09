Speed = int(input('Please enter your speed:'))
Time = int(input('Please enter your time:'))
Distance = Speed * Time
if Speed > 0 and Distance <= 100:
    print('You are already completed', Speed, 'km.', 'Keep it up')
elif Speed < 0 and Distance <= 100:
    print('You are already completed', Speed, 'km.', 'Hurry up')
else:
    print('Congratulations! You are already finished 100km')
