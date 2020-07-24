# random list of integers python

import random

def randomList(size, range=1000):
    lst = []
    i = 0
    while i < size:
        lst.append(random.randrange(range))
        i += 1
    return lst
