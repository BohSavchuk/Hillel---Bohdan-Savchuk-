import time


def timer(func):
    """
    The decorator helps to count down 3 seconds before show current time
    Args(func):None

    Returns: wrapper

    """
    def wrapper():
        sec = 3
        while sec > 0:
            time.sleep(1)
            print(sec)
            sec -= 1
        func()
    return wrapper


@timer
def current_time():
    print(time.strftime('%H:%M'))





current_time()