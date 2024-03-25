'--------------------------Comprehensions---------------------------'
# генератор с помощбю которого можно создать последовательность используя цикл for в одну строку

# range
# []
# {}
# {:}

# результат for элемент in последовательность


# list_ = [i if i % 2 == 0 else i*2 for i in range(1,11)]
# print(list_) 

'если в comprehension добавлять условия там их бывает 2 вида'
'1 - тернарный оператор пишется перед циклом так как используем if и else'
'2 - фильтр пишется после цикла так как используется только if'


list_1 = [12, True, None, 'hi', 0, 'makers', 'world']
list_2 = [i for i in list_1 if type(i) == str ]
print(list_2)

a = 12
print(type(a))


'-----------------------------------------------Виды  comprehensions-------------------------------'
'1 - list comprehension'
'2 - dict comprehension'
'3 - set comprehension'

'Dick comprehension'
dict_1 = {}
dict_2 = {i:i**2 for i in range(1,11)}
print(dict_2) # {1:1, 2:4, 3:9, ,,,,}

'Дан словарь поменяйте клюси значения с помощью comprehension'
# dict_1 = {'a':1, 'b':2, 'c':3}
# dict_2 = {v:k for k, v in dict_1.items()}
# print(dict_2)

'Дан словарь где значения списки из чисел создайте словарь где  значения будут '
# dict_1 = {
#     'a':[1,2,3],
#     'b':[12,0,1],
#     'c':[32,0,0,10]
# }
# dict_2 = {k:sum(v) for k, v in dict_1.items()}
# print(dict_2) # {'a':6, 'b':13, 'c':42}


'Set comprehension'
# set_1 = {i for i in range (1,11)}
# print(set_1) # (1,2,3,4,5,6,7,8,9,10)

# set_1 = {i for i in 'makers'}
# print(set_1) # {'m', 'a', 'k', 'e', 'r', 's'}

# set_1 = {2, 3, 4, 15, 1}
# set_2 = {i**2 for i in set_1 } 
# print(set_2) # {1, 225, 4, 9, 16}

# set_1 = {1, 12, 'hi', 34, True, 'makers'}
# set_2 = {i for i in set_1 if type(i) == str}
# print(set_2)

set_1 = {12, 'hi', '34', True, 10, '23', 'makers'}
set_2 = {int(i) if i.isdigit() else i for i in set_1 if type(i) == str}
print(set_2) # {'34', '23'}


'Создайте словарь где ключи будут от 1 до 5 а значениями списки от 1 до этого числа'

dict_1 = {i: [i for i in range(1,i+1)] for i in range(1,6)}
print(dict_1)
# [1:[1], 2:[1,2], 3:[1,2,3], 4:[1,2,3,4], 5:[1,2,3,4,5]]