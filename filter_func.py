# Функція filter() використовується для фільтрації об'єктів ітерації, 
# таких як списки або кортежі, за допомогою заданої функції. Вона створює ітератор, 
# який містить тільки ті елементи об'єкта ітерації, для яких функція-фільтр повертає True.

# Синтаксис filter():
#filter(function, iterable)
# function - функція, яка визначає, чи слід включати елемент у результат. 
# Ця функція повинна приймати один аргумент і повертати булеве значення True або False.
# iterable - об'єкт ітерації (наприклад, список, кортеж), елементи якого будуть перевірятися функцією function.

# Наприклад, виведемо список чисел, які є парними в інтервалі від 1 до 10:
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))


# Не обов'язково використовувати lambda функцію.
# У цьому прикладі filter() використовує функцію is_positive для відбору тільки додатних чисел:
def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))


# Інший приклад, давайте відфільтруємо з рядка літери, щоб залишилися лише літери нижнього регістру:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)



# Розглянемо, як можна замінити filter() на list comprehensions:
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)


# Для рядка літер:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)
