# Каррінг (currying) — це техніка в програмуванні, коли функція, яка приймає кілька аргументів, 
# перетворюється на послідовність функцій, кожна з яких приймає один аргумент. 
# Названа на честь логіка Гаскеля Каррі, каррінг дозволяє зробити функції більш гнучкими 
# і сприяє створенню високо модульного та читабельного коду.
from typing import Callable, Dict

# Припустимо, у нас є функція, яка приймає два аргументи:
def add(a, b):
    return a + b

# Тепер ми можемо перетворити цю функцію в каррінгову версію, яка приймає один аргумент і повертає іншу функцію:
# Застосувавши каррінг до цієї функції, ми перетворимо її на двій функції, кожна з яких приймає по одному аргументу:
def add1(a):
    def add_b(b):
        return a + b
    return add_b

# Використання:
add_5 = add1(5)
result = add_5(10)
print(result)

# Тут функція add приймає перший аргумент a і повертає функцію add_b. 
# Сама функція add_b приймає другий аргумент b і повертає результат a + b. 
# Фактично ми перетворили виклик функції add на виклик двох функцій.


# Приклад 2:
# Припустимо, у нас є функція для обчислення знижки на товар. Ця функція приймає відсоток знижки і остаточну ціну товару.
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)
# Тепер перетворимо цю функцію в каррінгову версію:
# Використовуючи каррінг, ми можемо створити більш гнучку структуру для роботи з різними типами знижок.
# Перетворимо функцію apply_discount, використовуючи каррінг. 
# Це дозволить нам створити "замовлені" функції для різних рівнів знижок, кожна з яких буде приймати тільки ціну товару.

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount1(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount1

# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price1 = ten_percent_discount(500)  # 450.0
print(discounted_price1)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)
# Таким чином, за допомогою каррінгу, ми розділили функцію на дві частини. 
# Спочатку ми створюємо функції з певним відсотком знижки ten_percent_discount та twenty_percent_discount, 
# а потім використовуємо ці функції для обчислення зниженої ціни. Це робить код більш гнучким 
# і дозволяє легко створювати функції для різних рівнів знижок.



# Приклад 3:
# створити словник, де ключами будуть назви знижок, 
# а значеннями — відповідні функції обчислення знижки, створені за допомогою каррінгу. 
# Це дозволить нам легко вибирати потрібну функцію знижки зі словника.
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

# Ми створюємо словник discount_functions, де кожному типу знижки "10%", "20%" та "30%" відповідає функція з каррінгом, 
# що обчислює знижку. І тепер щоб застосувати знижку, ми вибираємо потрібну функцію зі словника 
# за допомогою ключа discount_type і передаємо їй ціну товару.
