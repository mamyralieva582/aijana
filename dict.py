'=============================Словари=========================='
# dict - изменяемый, итерируемый, неупрядочный, [псевдопорядок] неиндексируемый тип данных для хранения данных в парах {ключ:значение}
user = {'name':'Anonym', 'age':30, 'last_name':'Makers'}
print(user)
# print(user['name']) # Anonym
print(user['age']) # 30
print(user['last_name']) # Makers


# ключами в словаре могут быть только неизменяемые типы данных
# ключами в словарях должны быть уникальными

'==========================================Создание словарей====================================='
# dict_ = {'a':1, 'b':2}
# dict_ = dict([('a', 1),('b', 2)])
# print(dict_)
# dict_ = dict(['a1', 'b2', 'c3'])
# print(dict_) # {'a':'1', 'b':'2', 'c':'3'}

# dict_ = {}
# dict_['name'] = ['makers']
# dict_['age'] = 50
# dict_['last_name'] = ['bootcamp']
# print(dict_)

'========================Методы словаря==========================='

'get -m это метод который получает значение по ключу если указанного ключа нет то выходит None-по умолчанию мы можем его поменять'

user = {'name':'Anonym', 'age':15, 'last_name':'Makers'}
# print(user['id']) # error - Keyerror
# print(user.get('id')) # None
# print(user.get('id', 'Такого ключа нет')) # Такого ключа нет


'pop - удаляет пару по ключу и возвращает значение'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.pop('b')
# print(dict_) # {'a':1, 'c':3}
# print(popped) # 2


'popitem - удаляет последнюю пару и возвращает ее'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_) # {'a':1, 'b':2}
# print(popped) # 2 op


'update - расширяет словарь из второго словаря'

# dict_1 = {1:'a', 2:'a'}
# dict_2 = {2:'b', 3:'b'}
# dict_1.update(dict_2)
# print(dict_1) # {1:'a', 2:'b', 3:'b'}


'clear - очищает словарь'
# dict_ = {'a':1, 'b':2, 'c':3}
# dict_.clear()
# print(dict_) # {}


'fromkeys - метод для создания нового словаряб изпользуя список ключей'

# dict_ = dict.fromkeys('hi')
# print(dict_) # ['h':None, 'i':None]
# dict_2 = dict.fromkeys(['hi', 123, True], 0)
# print(dict_2) # {''hi':0, 123;0, True:0}


'keys, values, items'
# keys - метод, который возвращает все ключи
# values - метод, который возвращает все щначения
# items - метод, который возвращает пары ключь и значение в виде tuple

w
# user = {'name':'Anonym', 'age':15, 'last_name':'Makers'}
# for i in user:
    # print(i)

# for key in user:
#     print(key) # при итерации словаря будут приходить ключи
# for value in user:
#     print(value)

# for value in user.values():
#     print(value) # при итерации словаря с методом values(, приходят значения)


# for item in user.items():
#     print(item) # при операции словаря с методом items(), приходит tuple с ключем и зн

# dict_1 = {1:'a', 2:'b'}
# for k, v in user.items():
#     dict_2[v] = k
#     print(dict_2)

