
# print(9//2,-9//2,9//-2,-9//-2)
# print(9%2,-9%2,9%-2,-9%-2)

# print(bin(25))

# print(~-25)

# number = int(input())
# for i in range(number):
#     print(f'{'*'*(i+1):>{number}s}')

# dirt =  dict(zip(['a','b'],[1,None]))
# dirt.update([['d',10]])
# dirt.update({1:1,2:2})
# dirt.setdefault('c',100)
# print(dirt)
# print(dirt.items())

# set = {1,2,3}
# set |= {2,3}
# print(set)

# table = str.maketrans('aeiou', '12345')
# print('apple'.translate(table))

# print('hello'.zfill(10))
# print('hello'.rjust(10,'0'))
# print('hello'.upper())
# print('%05.2f'%2.33)
# print('{0:>10}'.format('hello') )
# print('{0:1>10}'.format('hello') )
# print('{0:0>10.2f}'.format(1))
# print('{0:010.2f}'.format(1))
# print('{0:03d}'.format(1))

# dict = dict()
# dict.update(a=1)
# print(dict)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zipped = zip(list1, list2)

# dict.update(zipped)
# print(dict)
# dict2 = dict.fromkeys(list1)
# print(dict2)

# a=1
# print('{a}'.format(a=11))

# with open('score.txt','r',encoding='utf-8') as file:
#     for i in file:
#         print(i.strip('\n'))

# with open('score.txt','r',encoding='utf-8') as file:
#     print(file.read())


# with open('score.txt','r',encoding='utf-8') as file:
#     print(file.readlines())

b = 1
a = b

print(a,b)