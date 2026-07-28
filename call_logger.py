from datetime import datetime

def logger(func):
    def wrapper():
        print(f"Function Name : {func.__name__}")
        print(f"Called At     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return func()
    return wrapper


@logger
def greet():
    print("Hello! Welcome to Python Decorators.")

greet()