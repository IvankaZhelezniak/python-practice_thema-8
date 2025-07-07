# Дуже важливо при створенні декораторів використовувати модуль functools, 
# це необхідно для збереження метаданих оригінальної функції, яку ми декоруємо. 
# Функція functools.wraps допомагає в цьому, зберігаючи інформацію про оригінальну функцію, як-от ім'я функції та документацію.
from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)

# У цьому прикладі functools.wraps(func) застосовується до внутрішньої функції inner. 
# Вона "копіює" метадані (ім'я функції, документацію тощо) від func до inner. 
# Завдяки цьому, коли ми викликаємо print(complicated.__name__),
#  ми отримуємо метадані оригінальної функції complicated, а не функції inner з декоратору logger.
