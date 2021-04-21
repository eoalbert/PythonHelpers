""" Default python decorator implementation. """

import functools


def decorator(func):
    """Simple decorator without arguments"""

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

def repeat(num_times):

    def decorator_with_arguments(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            #Do...
            for _ in range(num_times):
                result = func(*args, **kwargs)
            #Do after...
            return result
        return wrapper
    return decorator_with_arguments


@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')
