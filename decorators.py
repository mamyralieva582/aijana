'-----------------------------Декораторы-------------------------------'
# функция высшего порядка - функция котороя принимает в аргументы другую функцию создает ынутри себя функцию и возвращает функию 

# def func1():
#     ...
# def func2(a): # функция высшего порядка так как принимает другую функцию в аргументы 
#        a()

# func2(func1)

# декораторы это функции высшего порядка котороя нужна чтобы расширить функцианал другой функции не изменяя ее (функция обертка)


# def glushitel(func):
#       def wrapper(*args, **kwargs):
#             text = func(*args, **kwargs)
#             return text + 'тихо'
#       return wrapper 


# def gun():
#       return 'Стреляет'

# wrapper = glushitel(gun)
# result = a()
# print(result)

# def gun():
#       return ('Стреляет')
# print(gun)

# def gun():
#       retuen('Стреляет')


# from datetime import datetime

# def func_start_time(func):
#     def wrapper():
#         time = datetime.now().strtime('%d, %m, %Y, %H:%M')
#         print(f'Наша функция запустилась (time_)')
#         func()
#     return wrapper 

# @func_start_time
# def func():
#       print('hi')

# @func_start_time
# def func1():
#       print('hello')

# func()
# func1()

