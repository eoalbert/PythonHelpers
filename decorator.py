""" Default python decorator implementation. """

import functools


def decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #Do...
        result = func(*args, **kwargs)
        #Do after...
        return result
    return wrapper


@decorator
def func(a,b):
    return a+b