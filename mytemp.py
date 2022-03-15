import datetime


FAKE_LIST = [i for i in range(1000000)]
FAKE_TUPLE = (i for i in range(1000000))


def t(func):
    def wrapper(*args):
        start = datetime.datetime.now()
        for i in range(100):
            func(*args)
        end = datetime.datetime.now()
        duration = end - start
        print(duration)
        return duration
    return wrapper

@t
def find(collection):
    result = False
    for i in collection:
        result = i == 98999
        if result:
            break
    return result


find(FAKE_LIST)
find(FAKE_TUPLE)