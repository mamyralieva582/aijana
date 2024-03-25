'------------------------Set--------------------------'
# множестваб изменяемый неупрядоченный итерируемый тип данных предназначенный для хранения уникальных значенийю Множества могуть хранить в себе только неизменяемый тип данных Если внутри set използуется tuple, то и внутри tuple должны быть неизменяемые  типы данных({1, 2, 3, 23('str', 12, True)}) В set работает правило - FIFO (firset in firset out)

# set_1 = {1, 0, True, 'hi'} # True
# set_2 = {True, 0, 1, 'hi'} # 1
# print(set_1, set_2)

'--------------------------FIFO/LIFO----------------------------------'
# FIFO - fist in first out (очередь в банк выйдет первым тот кто первым встал вочередь)
# LIFO - last in first out (стопка бумагб выйдет та бумага которую вы поставили)

'----------------------Методы set------------------------'

'add - добавляет элементы в set'
# set_1 = {1,2,3}
# set_1.add(3) # {1,2,3} ничего не изменится
# set_1.add(5) # {1,2,3,5}
# print(set_1) # {1,2,3,5}

'pop - удаляет случайный элемент из set(FIFO)'
# set2 = {1,2,3}
# popped = set2.pop()
# print(set2)  # {2,3}

'remove - удаляет элемент из seta по значению'
# set3 = {1,2,3}
# set3.remove(3)
# print(set3)

print(dir(set))

'union - обединяет set1 и set2'
# set1 = {1,2,3}
# set2 = {4,5,6}
# print(set1.union(set2))
# print(set1)

'update - обединяет set1 и set2 и сохзаняет изменения в set1'
# srt1 = {1,2,3}
# set2 = [4,5,6]
# set1.update(set2)
# print(set1)

'difference (-) - находит разницу из set1 при помощи set2'
# set1 = {1,2,3}
# set2 = {4,5,6}
# print(set1.difference(set2)) # (1,2)  
# print(set2.update(set1)) # (4,5)
# print(set1 - set2) # (1,2)
# print(set2 - set1) # {4,5}

'symmetric_difference - '
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.symmetric_difference(set2)) # {1,2,4,5}

'intesection (&) - находит схожие элементы из двух сетов set1, set2'
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1.intersection(set2)) # {3,4}
# print(set1 & set2) # {3,4}e x
