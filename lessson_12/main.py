# def sum_x_Y(x, y):
#     return x + y
#
# x = lambda x, y: x + y
# result = x(1,2)
# print(result)

# def double(x):
#     return x * 2
#
# m_list = ["1", "2", "3", "4", "5"]
# numbers = map(int, m_list)
# m_numbers = list(numbers)
# double_numbers = map(double, m_numbers)
# double_numbers_2 = map(lambda x: x * 2, m_numbers)
# print(list(double_numbers))
# print(list(double_numbers_2))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# even_numbers = list(
#     map(
#         lambda x: x * 2,
#         filter(
#             lambda number: number % 2 == 0,
#             numbers
#         )
#     )
# )
# print(even_numbers)


# def other_function(x):
#     print("Работает первая функция", x)
#     def inner_function(y):
#         print("Работает вторая функция", y, x)
#         return x + y
#     return inner_function
# # varibale = other_function(5)(10)
# inner = other_function(5)
# variable = inner(10)
# print(variable)
# import time
#
#
# def get_time_of_work_function(func):
#
#     def inner(x, y):
#         start = time.time()
#         result = func(x, y) # sum_x_y
#         end = time.time()
#         print("Время работы функци", end - start)
#         return result
#     return inner
#
#
# @get_time_of_work_function
# def sum_x_y(x,y):
#     print("Функция выполняется ожидайте")
#     time.sleep(5)
#     return x + y
#
#
# sum_x_y(5, 5)


# def repeat(count): # Прием параметра для декоратора
#
#     def decorator_repeater(func): # Приеем функции
#         def wrapper(*args, **kwargs): # Прием параметров функции
#             for i in range(count):
#                 print(f"Запуск номер {i}")
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator_repeater
#
# @repeat(4)
# def say_hello():
#     print("Hello")
#
# say_hello()


# def get_some(*args):
#     print(*args)
#
# get_some(1,2,3,4,4,5,6)

# def get_some(name, last_name):
#     print(name, last_name)
#
# get_some('John', 'Smith')
# get_some(last_name="H", name="df")

def get_some_too(*args,**kwargs):
    print(args)
    print(kwargs)

get_some_too("sdf","sdfsdf",name="dsf", last_name="sdfs")