import time
import threading


def numberCounter(x):
    for i in range(x):
        time.sleep(1)
        print(i)

def halfNumberCounter(y):
    for i in range(y):
        time.sleep(0.5)
        print(i)


threading.Thread(None,numberCounter(7))
threading.Thread(None,halfNumberCounter(5))


