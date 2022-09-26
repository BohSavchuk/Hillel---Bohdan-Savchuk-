import json
import time

def track_duration_task_2():
    track_duration = 0
    with open('acdc.json', 'r') as file:
        album = json.load(file)
        track = album['album']['tracks']['track']
    for i in track:
        track_duration += int(i['duration'])
    result = time.gmtime(track_duration)
    return time.strftime('%H:%M:%S', result)


print(track_duration_task_2())
