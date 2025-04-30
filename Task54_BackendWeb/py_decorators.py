import time


# Python decorators: A function inside another one
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hi")

@delay_decorator
def say_bye():
    print("Bye")

# decorated_func = delay_decorator(say_bye)