# password = input()
# confirmedPassword = 'aBc'

# arePassSame = password == confirmedPassword

# print(arePassSame)

# x = 5
# y = 1
# result = x < y
# print(result)

# arr='Abc'
# print((arr.lower()))

# if int(input()) > 1:
#     print(1 )
# else:
#     print(-1)

# def get_country():
#     country = input('Please enter a country name: ')
#     return country

# def print_in_console(country, capital):
#     print('The caital of {} is {}'.format(country, capital))

# def country_to_capital():
#     country = get_country()

#     capital = ''

#     if country == 'France':
#         capital = 'Paris'
#     elif country == 'Germany':
#         capital = 'Berlin'
#     elif country == 'Itary':
#         capital = 'Rome'

#     print_in_console(country, capital)

# country_to_capital()

# dict = {'a':'apple', 'b':'base', 'c':'cap'}
# print(dict.items())
# for i in dict.items():
#     print(i)

# import time
# n = 100000
# start = time.time()
# squares = [k*k for k in range(1, n+1)]
# end = time.time()
# print(f'{start-end}')

# start = time.time()
# squares = []
# for k in range(1, n+1):
#     squares.append(k*k)
# end = time.time()
# print(f'{start-end}')

# import time
# start = time.time()
# document = 'Helloabcacdafdqwedfsfsadfasfdasdfsfrqwefoqwjfoqwj;qweiofjoqjef'
# letters = ''
# for c in document:
#     if c.islower():
#         letters += c
# end = time.time()
# print(f'{letters} {end-start:0.7}')

# import sys

# empty_list = []
# int_list = [1]

# print("빈 리스트의 크기:", sys.getsizeof(empty_list), "바이트")
# print("정수를 포함한 리스트의 크기:", sys.getsizeof(int_list), "바이트")

arr = [1,2,3,4]
ext = [5,6]
arr.extend(ext)
print(arr)
ext[1]= 7
print(arr)
print(ext)

