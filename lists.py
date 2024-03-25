'----------------------------List---------------------'
# списки - изменяемый индексируемый упрядоченный итерируемый тип данных предназначенный для хранения любых данных в опроделенном порядке 

list_1 = [1, 5 , 13,'hello', True, [0, 0]] 
        # 0  1    2    3       5      6
list_1[4] # 'hello'
list_1[-1] # None
list_1[-1][-1] # 0
list_1[3][-2] # l
# print(list2)
list_1[5] # [0,0]


'range(start, end(не включительно), step)- это функция генератор которая генерирует\создает диапозон от start до end (не включительно)'

list('hello') #-> ['h' 'e ' 'l' 'l' 'o']
list_2 =  list(range(0, 101)) # [0, 1, 2, ,,,,,,,,99,100]

# print(list(range(0, 11)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] шаг 1
# [0, 2, 4, 6, 8, 10] шаг 2
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] шаг -1

'------------------------Методы списков--------------------------'
# 'append - добавление элемента в конец списка'

# list_ = []
# list_.append(1)
# list_.append('hello world')
# list_.append(True)
# print(list_) # [1, 'hello world', True]

'pop - удаление элемента из списка по индексу возвращает удаленый элемент. Если не указать индекс то удалить с конца'

# list_ = [90, True, None, 'Hi']
# popped = list_.pop(1)
# print(list_) # [90, None. 'Hi]
# print(popped) # True

'remove - это удаление элемента из списка по элементу(значению)'

# list_ = [1, 2, 3, 1, 4, 5, 99, 0, -11]
# list_.remove(5)
# print(list_)

'count - считает количество прнятого элемента в списке'

# list_ = [1, 23, 1, 4, 5, 6, 'hi', 'hi', 1, 7, 8, 7, 'Hi', 1]
# print(list_.count(1)) # 4
# print(list_.count(7)) # 2
# print(list_.count('hi')) # 2

'index - находить вам под каким индексом находиться элементю возвращает индекс первого вхождения принятого элемента'

# list_ = ['hi', 1, 341, 2, 0, 2, 1, 99, 10]
# print(list_.index(0)) # 4

'extend - расширяет список при помощи другого списка'

# list_1 = [1, 2, 0]
# list_2 = [0, 0, 0]
# list_1.append(list_2) # [1, 2, 0[0, 0, 0]]
# print(list_1)
# list_1.extend(list_2) # [1, 2, 0, [0, 0, 0] 0, 0, 0]
# print(list_1)

'reverse - изменяет список растовляя его элементы в обратном порядке'

# list_ = ['hi', 1, 2, 3, True]
# list_.reverse()
# print(list_) # [True, 3, 2, 1, 'hi']

'sort - сортирует список состоящий из элементов одного типа данных'

list_ = [12, 4, 1, 0, 25, 7]
list_.sort(reverse=True)
print(list_) 

# list_ = ['c', 'b', 'a', 'A', 'B']
# list_.sort()
# print(list_) # ['c', 'b', 'a', 'A', 'B']

'clear - очищает список'
# list_ = [12, 42, 1, 'hi', 0, False, True]
# list_.clear()
# print(list_)

# len([12, 4, 5, [1, 2, 3]]) # 4
#print(len)


# a = 10
# b = 5
# c = 2


# a, b, c = 10, 5, 2
# print(a, b, c)

# list_ = [23, 'hi', 4, 0, 'makers']
# for i in list_:
#     print(i)

# meshok = ['картошка', 'лук', 'лук', 'картошка', 'лук']

# paket1 = []
# paket2 = []

# for ruka in meshok:
#     if ruka == 'картошка':
#        paket1.append(ruka)
#     elif ruka == 'лук':  
#        paket2.append(ruka)

# print(paket1)
# print(paket2)

