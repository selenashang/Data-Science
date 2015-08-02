import random

"""Chooses random elements if you are already given the array of items"""
def random_element(a, N):
        return a[int(random.random() * N)]

"""The n-th element of the iterator has a 1/N of being kept."""
def random_element_iterator(iterator):
    N = 0
    for item in iterator:
        N += 1
        #Determine if 1/N chance succeeds
        if random.random() * N < 1:
            element = item
    return element

"""Retrieve k random numbers from an array of undetermined size, also known as reservoir sampling"""
def random_subset(iterator, k):
    result = []
    N = 0
    for item in iterator:
        N += 1
        if len( result ) < k:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < k:
                result[s] = item

    return result

