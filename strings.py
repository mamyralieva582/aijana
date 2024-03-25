'---------------------String----------------------'

# строки - неизменяемый тип данных который предназначен для хранения текстаб заключенного в олинарные либо двойные кавычки

string1 = 'строка с одинарными кавычкам'
string2 = "строка с двойными кавычками"
string3 = "Don't" # внутри двойных кавычек все одинарные кавычки - просто часть текста 
string4 = 'Название магазина'
string5 = ''''''
# Многострочный текст ''''''
# в одинарных кавычках
# Тут можно использовать и одинарные и двойные кавычки 
# '' ''
# string6 = " " "
# Много стройный текст в двойных кавычках 
# Тут можно использовать и одинарные и двойные """"
string7 = 'hello' + 'world' #helloworld
print(string7)

string8 = 'A'* 20 
print(string8)

'---------------------------Экранизация строк---------------------'
'\n' #перенос на новую строку
print('hello world') # hello world
print('hello\nworld') #hello
                     # world
print('he\nello world') #he
                       #ello world
'\t' # табулация(несколько пробелов)
print('hello\tworld') #hello   world
print('he\tllo world') #he   llo world


'\v' # перенос на новую строку со смещением вправо на длинну предыдущей строки 
print('hello\vworld\vmaktrs') #hello
                              #     world
                              #          makers
'\r' # перенос каретки в самое начало строки 
print('hello world\rMa') #Mallo world


'\'' # отобрежение '
"\"" # отоброжение "
#("Home\\'Makers'"


'\\' #
print('команда \n переносит строку')





'--------------------------Форматривание строк ---------------'
title = 'IPhone 15'
price = 115000
shop = 'Makers'
# print('Я купил title за price $')

'1,' 

# f - строка 
print(f'Я купил {title} за {price}$, в мвгвзине {shop}')

'2. %s'
print('Я купил %s за %s$, в магазине %s'%(title, price, shop))

'3. str.format' 
print('Я купил {} за {}$, в магазине {}'.format(title, price, shop))


'-----------------------Методы строк----------------------'
# методы - функции которые относятся к определенному типу данных(классу) к ним мы обращаемся через точку

print(dir(str)) 

string = 'Hi'
  
print(string.upper()) # HELLO WORLD
print(string.lower()) # hello world
print(string.swapcase()) #HELLO WORLD

print(string.title()) # Hello World
print(string.capitalize()) # Hello world

print(string.islower()) #True
print(string.isupper()) #False 

print(string.center(12)) #'     Hi     '


string = 'hello world'
# print(string.count('l')) # 3
# print(string.count('el')) # 1
# print(string.count('o w')) # 1
# print(string.count('hello')) # 1


# print(string.startswith('h')) # True
# print(string.startswith('H')) # False 
# print(string.startswith('hello')) # True
# print(string.startswith('h')) # True

string = 'makers'
# print(string.isalpha()) # True, проверяет на буквы
# print(string.isdigit()) # False, проверяет на числа
# print(string.isalnum()) # False, проверяет является ли строка числом или буквой или и числом и буквой если есть символ то вернет False


string = 'hello world makers bootcamp'
print(string.split('o')) #'he [hello', 'world', 'makers', 'bootcamp']

# print(string.startswith('h')) # True 

# print(string.replace('l','m'))

# string = '  $12   hi$$$$$$$$$'
# print(string.strip('$')) 


# ''.join(strihg) # strihg - в данном случае это list[]

'-----------------------Индексы-------------------------'
# это порядковый номер элемента в последовательности (индекс начинается с 0)

# -11-10-9-8-7-6-5-4-3-2-1
#    'h e l l o  w o r l d'
#     0 1 2 3 4 5 6 7 8 9 10

string = 'hello world'
print(string[0]) #'h'
print(string[-1]) #'d'
print(string[5]) #''

# срез [start:end](не включительно) :step]
string[6:10] # worl
string[:5] # hello
print(string[::2]) #hlowrd
print(string[::-1]) #dlrow ollex
print(string[::-2]) #drwlh


string = '      Как прекрасен этот мир     '
str = string.strip('')
len = len(str)
print(str, len)