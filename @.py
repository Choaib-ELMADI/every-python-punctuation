import time


def tictoc(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{ func.__name__ } executed in { '{:.2f}'.format(end - start) } seconds")

    return wrapper


@tictoc
def do_something_1():
    print("Doing something 1")
    time.sleep(2)
    print("Done something 1")


@tictoc
def do_something_2():
    print("Doing something 2")
    time.sleep(3.5)
    print("Done something 2")


do_something_1()
do_something_2()
