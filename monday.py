#1задание
#a = [1,2,2, 4,11,2, 3, 1]
#print(list(set(a)))

#2 задание
# a = ['John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom']
# a.pop(0)
# a.pop(4)
# a.pop(3)
# print(a)

#3
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.reverse()
# print(a)

#4
# list1 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'october', 'sunday']
# print(list1)
# list2 = list1.copy()
# list2.remove('october')
# list2.insert(5, 'saturday')
# print(list2)

# #5
# list1 = (input("Ввести слова через пробел: "))
# a = list1.split()
# a.sort(key=len)
# print(a)

#6
# dict1 = {1: 2, 3: 4, 5: 6, 7: 8 }
# print(dict1.get(3))



#7
# a = {'Введите свое имя'}
# b = {'пайтон' }
# a.update(b)
# print(a)

#8
# name = {'Aktilek': 'Jumagylov', 'John' : 'Seena' }
# user = list(name.keys())
# user.sort()
# print(user)

#9

# a = input('введите слово')
# b = {}
# c = b =a
# if len (c) == 0:
#     print('пустой')
# else:
#     print('не пустой')


#10
# nums = [1, 2, 3]
# nums2 = [4]
# nums3 = {5, 6}
# nums4 = [7]
# nums.extend(nums2)
# nums.extend(nums3)
# nums.extend(nums4)
# print(nums)
# nums = tuple(nums)
# print(nums)

#11
# login = input ('Введите ваш логин')
# password =  input('Введите ваш пароль')
# dict1 = {'login': 'password'}
# print(dict1)

#12

# a = input('введите букву')
# if len(a) >1:
#     print('меньше букв')
# elif a == 'a' or a =='u' or a=='y' or a == 'i' or a == 'o':
#     print('это  глассная')
# else:
#     print('это согласная')

#13
# n = int(input('Введите количество яблок в корзине: '))
# x = int(input('Введите количество студентов: '))
# if n > x:
#     def func1():
#         print(f'Каждый студент получил по {n // x} яблок' + ' ' + f'остаток в корзине {n % x}')
#     func1()
# if x > n:
#     ost = n - n // x
#     print(f'Студентов {x}, яблок в корзине {n}, остаток яблок в корзине {ost}')

#14
# a = int(input('введите кол-во учеников'))
# a = a // 2
# b = a % 2
# c = b + a
# print(f' {a} сколько парт нужно купить' )


#15

# age = int(input('Возраст собаки: '))
# sm = str(input('Размер собаки: (маленькая/средняя/большая)'))
# if  sm =='маленькая' :
#     s = age * 9
#     print(s , 'Человечких лет')
# if sm == 'средняя':
#     s = age * 10,5
#     print(s, "Человеческих лет")
# if sm == 'большая' :
#     s = age * 12,5
#     print(s, 'Человеческих лет')






#16

# a = int(input('введите числа'))
# b =  int(input('введите числа'))
# с = int(input('введите числа'))
# if a > 10 and a > 10 and a  > 10:
#     print('Yes')
# else:
#     print('no')

#17
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print((a > 0) + (b > 0) + (c > 0))
# print('положительных чисел')





#18
# a = int(input('введите первое число '))
# b = int(input('введите второе число'))
# c = int(input('введите третье число'))
# if a > 0:
#     a = 1
# else:
#     a = 0
#
# if b>0 :
#     b = 1
# else:b = 0
#
# if c > 0:
#     c = 1
# else:c = 0
#
# print (f'в  списке {a + b + c} положитьельных чисел')


#19
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# m = a
# if m < b:
#     m = b
# if m< c:
#     m = c
#     print(m)


#20
# num1= int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# if num1 > num2   and num1 < num3:
#     print('первое число среднее')
# elif num2 > num1 and num2 < num3:
#     print('второе число среднее')
# elif num2 > num1   and num3 <  num2:
#     print('третье число среднее')