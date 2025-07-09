# Стандартна структура декоратора

def timer(func):
    def wrapper(*args, **kwargs):
        print("before")
        res = func(*args, **kwargs)
        print(res)
        print("after")

    return wrapper


@timer
def add(a, b):
    return a + b

add(1, 2)