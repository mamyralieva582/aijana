'                   Логические и условные операторы             '
# boolean - тип данных который имеет 2 значения
# true; (да истина) и False(нет ложь)

print(bool(0)) # False
print(bool(-10)) # True
print(bool(' ')) #True
print(bool('')) # False
print(bool(None)) # False

# Логические операторы - выражения, которые возвращают True, если вражения верное. False - если не верно

'равенства'
5 == 5 # True
5 == 7 #False

'не равенство'
5 != 10 # True
5 != 5 # False

'больше'
5  > 1 # True
0 > 10 # False

'меньше'
10 < 100 # True
0 < -10 # False
5 < 5 # False

'больше или равно'
5 >= 10 # False
10 >= 3 # True
3 >= 3 # True

'меньше или равно'
10 <= 5 # False
5 <= 5 # True
5 <= 5 # True  


'5' == 5 # True
'hello' == 'hello' # True
'hello' == 'Hello' # False

print('hello '==' hello') #True

'               And or Not                  '

# and - и 
# or - или 
# not - не

'AND - возвращает #True, если все выражения вернули #True  '

a = 5
b = 6

# True   и    #True
a == 5 and b == 6 # True

#False  и   # True
a == 5 and b == 6 #False

# True  и  # False
a == 5 and b == 2 # False

# False   и  # False
a == 1 and b == 1 # False


'OR - возвращает #True если хотябы один из выражений вернул #True, либо когда все выражения вернули #True '

c == 5 
d == 6

# True или #True
c == 5 or d == 6 # True

# False или # True
c == 1 or d == 6 # True

# True или # False 
c == 5 or d < 1 # True

# False или # False
c <= 1 or d > 1000 # False


'NOT - это частица не, которая меняет значение на противоположенное'

a = 10
b = 5

not False # True
not True # False 

#not False или False  и    True
not a == b or b > 10 and 10 == a # True

not not not not not 5 == 5 # False

not  5 != 5 # True 

bool([]) # False
bool('None') # True

'==========================Условные операторы==================='

# условные операторы это - конструкция которая используется для того чтобы при разных входных данных код работал по разному (в зависимости от условия)

pagoda = 'дождь'
if pagoda =='дождь':
       print('взял зонт')
elif pagoda == 'снег':
    print('взял шапку и шарф')
elif pagoda == 'солнце':
    print('взял очки')
else:
     print('сижу дома')



 # в одной конструкции мы можем использовать только один if
 # в одной конструкции мы можем использовать неограниченное кол-со elif или не использовать вообще 
# в одной конструкции мы можем использовать только один else или не использовать вообще 

 # Принять от пользоватля 
     
number = int(input('7'))
if number > 0:
     print('Число положительное')
elif number < 0:
     print('Число отрицательное')
else:
     print('Число 0')


'-------------------Тернарный оператор------------------'
# тернарный оператор - условия в одну строку 

# тело1 if условие1 else тело2

num = 10
if num > 0:
   message = 'Положительное число'
else:
     message = 'Отрицательное число или 9'
     print(message)

num = 9 
message = 'Положительное число' if num > 0 else 'Отрицательное число или 0' 
print(message)

