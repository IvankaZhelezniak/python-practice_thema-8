from typing import Callable, Dict

# Перше, це присвоїмо функцію змінній.
def my_function():
    print("Hello, world!")

f = my_function
f()
# Тепер ми можемо викликати функцію через змінну.


# Функції можуть бути аргументами інших функцій. Припустимо, 
# у нас є декілька функцій для обчислення різних математичних операцій. 
# Ми можемо створити функцію apply_operation, яка приймає іншу функцію, 
# як аргумент та використовує її для обчислення результату.

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)

# Коли ми додаємо функцію як аргумент, щоб додати типізацію до цих функцій у Python, 
# використовуються анотації типів з модуля typing. Функція apply_operation має, 
# вже знайомі нам анотації типів для a та b, 
# а ось для параметра operation анотована як Callable[[int, int], int]. 
# Це означає, що параметр operation це функція, яка приймає два цілі числа та повертає ціле число.



# Функції як об'єкт першого класу можуть повертати інші функції. 
# Наприклад, ми можемо створити функцію, яка генерує іншу функцію для підняття числа до заданого степеня.
def power(exponent: int) -> Callable[[int], int]:   # # Типізація функції
    def inner(base: int) -> int:     # Типізація внутрішньої функції
        return base ** exponent       # Піднесення до степеня
    return inner                      # Повернення внутрішньої функції

# Використання
square = power(2)    # Функція для піднесення до квадрату
cube = power(3)     # Функція для піднесення до кубу

print(square(4))     # Виведе 16, оскільки 4^2 = 16
# Виведе 64, оскільки 4^3 = 64
print(cube(4))
# У цьому прикладі функція power приймає ціле число exponent і повертає функцію inner,
# яка підносить число base до степеня exponent.



# І останнє: це зберігання функцій у структурах даних. 
# Наприклад, створимо словник, де ключами будуть назви операцій, а значеннями — відповідні функції.
# Визначення функцій
def add1(a: int, b: int) -> int:
    return a + b

def multiply1(a: int, b: int) -> int:
    return a * b

def power1(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power1(2)
cube = power1(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25

print(result_add)  
print(result_square)

# Наш словник operations містить посилання на всі чотири наші функції. 
# І тепер через operations виконуються операції add або square з відповідними аргументами. 
# Де ключ словника це назва наших функцій.

# Зверніть увагу, що тип Dict[str, Callable] означає словник, де ключі - це строки, 
# а значення - це об'єкти, що можна викликати. У контексті operations: Dict[str, Callable] це означає,
#  що словник містить назви операцій і посилання на функції, які виконують ці операції.

