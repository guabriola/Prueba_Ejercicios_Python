import datetime

def traza(n):
    def wrapped(*args):
        print(datetime.datetime.today())
    return wrapped


@traza('1234')
def factorial(n):
    total = 1
    for x in range(1, n + 1):
        total *= x
    return total


@traza('12')
def test():
    pass


factorial(3)
test()