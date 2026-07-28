def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                print("Error: All arguments must be positive integers.")
                return
        return func(*args)
    return wrapper


@validate_positive
def add(a, b):
    print("Sum =", a + b)


add(10, 20)      
add(-5, 10)     
add(15, "5")    