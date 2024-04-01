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

# arr = [1,2,3,4]
# ext = [5,6]
# arr.extend(ext)
# print(arr)
# ext[1]= 7
# print(arr)
# print(ext)

# arr = [1,2,3,4,5]
# arr1 = arr[1:3]
# print(arr1)

# def evalRPN(tokens):
#     stack = []
#     operators = {"+": lambda x, y: x + y,
#                  "-": lambda x, y: x - y,
#                  "*": lambda x, y: x * y,
#                  "/": lambda x, y: int(x / y)}

#     for token in tokens:
#         if token in operators:
#             y = stack.pop()
#             x = stack.pop()
#             operation = operators[token]
#             result = operation(x, y)
#             stack.append(result)
#         else:
#             stack.append(int(token))

#     return stack[-1]

# rpn_expression = ['1','2','3','+','4','5','6','*','-','7','*','+','-','8','9','*','+']
# print(evalRPN(rpn_expression))

# define a new type of exception for stack ADT
# class Empty(Exception):
#   ''' Error attempting to access an element from an empty container.'''
#   pass

# class ArrayStack:
#   ''' LIFO stack implementation using a Python List as underlying storage'''

#   def __init__(self):# constructor
#     ''' create an empty stack'''
#     self._data = []    # nonpublic list instance

#   def __len__(self):
#     ''' return the number of elements in a stack'''
#     return len(self._data)

#   def is_empty(self):
#     ''' Return True if the stack is empty'''
#     return len(self._data) == 0

#   def push(self, e):
#     ''' Add element e to the top of the stack'''
#     self._data.append(e)  # new item stored at end of a list

#   def top(self):
#     '''
#     Return the element at the top of the stack
#     Raise Empty Exception if the stack is empty
#     '''
#     if self.is_empty():
#       raise Empty('Stack is Empty')
#     return self._data[-1]           # the last item in the list

#   def pop(self):
#     '''
#     Remove and return the element from the top of the stack
#     Raise Empty excepion if the stack is empty
#     '''
#     if self.is_empty():
#       raise Empty('Stack is Empty')
#     return self._data.pop()

#   def __str__(self):
#     '''
#     A string representation of the stack
#     An arrow shows the top of the stack
#     '''
#     return ''.join(str(self._data)) +'>'
  
#   # Creating a stack
# def create_stack():
#     stack = []
#     return stack


# # Creating an empty stack
# def check_empty(stack):
#     return len(stack) == 0


# # Adding items into the stack
# def push(stack, item):
#     stack.append(item)
#     print("pushed item: " + item)


# # Removing an element from the stack
# def pop(stack):
#     if (check_empty(stack)):
#         return "stack is empty"

#     return stack.pop()

# # reversing data using a stack
# def reverse_file(filename):
#   ''' Overwrite given file with its conent line-by-line reversed'''

#   S = ArrayStack()
#   original = open(filename)
#   for line in original:
#     S.push(line.rstrip('\n')) # we will re-insert newlines when writing
#   original.close()

#   # Now we overwrite with contents in LIFO order
#   output = open(filename, 'w') # reopening file overwrites original
#   while not S.is_empty():
#     output.write(S.pop() + '\n') # re-insert newline characters
#   output.close()

# ###########
# file = open("initial.txt", 'w')
# file.write("I am going home.\n")
# file.write("Today is a holiday.")
# file.close()

# type initial.txt
# print('\n\n')
# reverse_file("initial.txt")
# type initial.txt

# import collections

# D = collections.deque()
# D.appendleft(15)
# D.appendleft(12); D.append(66)
# print(D)

# from collections import deque

# D = deque()
# D.appendleft(55)
# a = D.is_empty()
# print(a)

class Empty(Exception):
  ''' Error attempting to access an element from an empty container.'''
  pass

class LinkedStack:

    # class Node:#nested class
    #     __slots__=['_element','_next']

    #     def __init__(self, element, next):
    #         self._element = element #노드의 데이터
    #         self._next = next #노드의 포인터
    class Node:
        def __init__(self,element,next):
            self._element = element
            self._next = next
    
    # def __init__(self):
    #     self._head = None #헤드 노드                  
    #     self._size = 0 #노드 개수

    def __init__(self):
        self._head = None
        self._size = 0


    # def __len__(self):
    #     return self._size
    
    def __len__(self):
        return self._size

    # def is_empty(self):
    #     return self._size == 0

    def is_empty(self):
        return self._size == 0
    

    
    # def top(self):
    #     if self.is_empty():
    #         raise Empty('Stack is Empty')
    #     return self._head._element

    def top(self):
        if self._size == 0:
            raise Empty('Stack is Empty')
        return self._head._element
    
    # def push(self,e): #push할떄 노드를 만든다. self가 S가 된다. nested 클래스를 속성처럼 쓰는 구나 여기서 self._head를 노드로 만들었으니 self._head._element이런식으로 쓸수 있다.
    #     self._head = self.Node(e,self._head)
    #     self._size += 1

    def push(self,e):
        self._head = self.Node(e,self._head)
        self._size += 1

    # def pop(self):
    #     if self.is_empty():
    #         raise Empty('Stack is Empty')
    #     answer = self._head._element
    #     self._head = self._head._next
    #     self._size -= 1
    #     return answer
    
    def pop(self):
        if self._size == 0:
            raise Empty('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1 
        return answer

    # def __str__(self):
    #     ''' String representation of the stack'''
    #     arr = ''
    #     start = self._head
    #     for i in range(self._size):
    #         arr += str(start._element) +', '
    #         start = start._next

    #     return '<' + arr + ']'

    def __str__(self):
        arr = ''
        start = self._head
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next
        return '<'+arr+']'
            
if __name__ == '__main__':

  S = LinkedStack()
  S.push(10)
  S.push(15)
  S.push(3)
  S.push(17)
  S.push(0)
  S.push(2)
  print('Stack Length: ', len(S))
  print('Stack S: ', S)

  print('Pop :', S.pop())
  print('Pop :', S.pop())

  print('Stack Length: ', len(S))
  print('Stack S: ', S)