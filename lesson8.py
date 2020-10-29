#генераторы списков

# new_list  = [i for i in range(1, 21)]
# print(new_list)
#
# new_list2 = []
# for i in range (1, 21):
#     new_list2.append(i)
# print(new_list2)


# new_list_even = [num for num in range(1,21) if num % 2 == 0]
# print(new_list_even)
#
# new_list_odd = [num for num in range(1,21) if num % 2 == 1]
#print(new_list_odd)


#lambda это оператор созданий

# lambda _func = lambda x, y: x + y
# print(lambda_func(5,5))

# list1= ['1', '2', '3', '4','5', '6']
# new_list = list(map(int,list1))
# print(new_list)


# list_  = [x for x in range (1, 51)]
# def my_func(x):
#     return x * x
# new_list = list_(map(my_func, list_))
# print(new_list)


# list_  =  [1, 2, 3, 4, 5, 6, 7, 8,9]
#
# def my_func(element):
#     element = str(element) + 'element'
#     return element
#
# new_tuple = tuple (map(my_func, list_))
# print(new_tuple)

# text  =  'hello world'
# text2 =
# def new_ func(a):
#     a = a.upper
#     return a
#
# new_text =  str(map( new_func, text))
# print(new_text)


# mixed_list = ['мак', 'просо', 'мак', 'просо', 'мак', 'просо,' 'мак']
# zolushka =  list(filter(lambda x: x == 'мак', mixed_list))
#
# print(zolushka)


# def filter_odd_num(in_num):
#     if (in_num % 2) == 0:
#         return True
#     else:
#         return False
#
# nums = [1 ,2, 3, 4, 5, 6, 7, 10, 11]
# out_filter = filter(filter_odd_num, nums)
# print(list(out_filter))


#функция reduce

# from functools import reduce
# items =[1, 2, 3, 4, 5]
# sum_all = reduce (lambda x,y: x +y, items)
# print(sum_all)


#функция zip

# a = [1, 2, 3]
# b = 'xyz'
# c = (None, True, False)
# res = list(zip(a, b, c))
# print(res)


# names = ('Erkin', 'kirill', 'Aktilek')
# ages = [ 31, 28, 18]
# tel = [1234, 4567, 134256789]
# new_dict = dict(zip(names, ages ))
# new_tupie = tuple(zip(names, ages, tel))
# new_list = list(zip(names, ages, tel))
# new_set = set (zip(names, ages))
# print(new_dict)
# print(new_tupie)
# print(new_set)
# print(new_list)

#function enumerate
# list_ = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0]
# new_list = []
#
# for num in enumerate(list_):
#     new_list.append(num)
#
# print(new_list)
#
#
# text = 'hello world'
# for i in enumerate(text):
#     print(i)
#

# декароторы
#
# def wrapper_func():
#     def hello():
#         print('hello')
#     hello()
#
# wrapper_func()

# def decorator_func(func):
#     return 'DECORATOR'
#
# @decorator_func
# def  hello_world():
#     print('hello world')
#
# hello_world

def burger (func):
    def bur(*args, **kwargs):
        print('верхняя булочка')
        func (*args, **kwargs)
        print('нижняя булочка')
    return bur

def kotleta (k):
        def kot(*args, **kwargs):
            print('курочка')
            k(*args, **kwargs)
            print('говядина')
        return kot

@burger
@kotleta
def nachinka(cheese, tomatoes, cucumber, sous):
    print('\n', cheese, tomatoes, '\n', cucumber,'\n', sous, '\n')
nachinka('сыр','помидоры', 'огурцы','соус')


