import functools

##################################################
# Simple Function Decorator Template
##################################################
def decorator(func):
    """Function decorator without arguments"""

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

##################################################
# Function With Arguments Decorator Template
##################################################

def repeat(num_times):
    """Function decorator with arguments"""
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

##################################################
# Class Decorator Template
##################################################
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')