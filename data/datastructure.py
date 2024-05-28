# # # # # # password = input()
# # # # # # confirmedPassword = 'aBc'

# # # # # # arePassSame = password == confirmedPassword

# # # # # # print(arePassSame)

# # # # # # x = 5
# # # # # # y = 1
# # # # # # result = x < y
# # # # # # print(result)

# # # # # # arr='Abc'
# # # # # # print((arr.lower()))

# # # # # # if int(input()) > 1:
# # # # # #     print(1 )
# # # # # # else:
# # # # # #     print(-1)

# # # # # # def get_country():
# # # # # #     country = input('Please enter a country name: ')
# # # # # #     return country

# # # # # # def print_in_console(country, capital):
# # # # # #     print('The caital of {} is {}'.format(country, capital))

# # # # # # def country_to_capital():
# # # # # #     country = get_country()

# # # # # #     capital = ''

# # # # # #     if country == 'France':
# # # # # #         capital = 'Paris'
# # # # # #     elif country == 'Germany':
# # # # # #         capital = 'Berlin'
# # # # # #     elif country == 'Itary':
# # # # # #         capital = 'Rome'

# # # # # #     print_in_console(country, capital)

# # # # # # country_to_capital()

# # # # # # dict = {'a':'apple', 'b':'base', 'c':'cap'}
# # # # # # print(dict.items())
# # # # # # for i in dict.items():
# # # # # #     print(i)

# # # # # # import time
# # # # # # n = 100000
# # # # # # start = time.time()
# # # # # # squares = [k*k for k in range(1, n+1)]
# # # # # # end = time.time()
# # # # # # print(f'{start-end}')

# # # # # # start = time.time()
# # # # # # squares = []
# # # # # # for k in range(1, n+1):
# # # # # #     squares.append(k*k)
# # # # # # end = time.time()
# # # # # # print(f'{start-end}')

# # # # # # import time
# # # # # # start = time.time()
# # # # # # document = 'Helloabcacdafdqwedfsfsadfasfdasdfsfrqwefoqwjfoqwj;qweiofjoqjef'
# # # # # # letters = ''
# # # # # # for c in document:
# # # # # #     if c.islower():
# # # # # #         letters += c
# # # # # # end = time.time()
# # # # # # print(f'{letters} {end-start:0.7}')

# # # # # # import sys

# # # # # # empty_list = []
# # # # # # int_list = [1]

# # # # # # print("빈 리스트의 크기:", sys.getsizeof(empty_list), "바이트")
# # # # # # print("정수를 포함한 리스트의 크기:", sys.getsizeof(int_list), "바이트")

# # # # # # arr = [1,2,3,4]
# # # # # # ext = [5,6]
# # # # # # arr.extend(ext)
# # # # # # print(arr)
# # # # # # ext[1]= 7
# # # # # # print(arr)
# # # # # # print(ext)

# # # # # # arr = [1,2,3,4,5]
# # # # # # arr1 = arr[1:3]
# # # # # # print(arr1)

# # # # # # def evalRPN(tokens):
# # # # # #     stack = []
# # # # # #     operators = {"+": lambda x, y: x + y,
# # # # # #                  "-": lambda x, y: x - y,
# # # # # #                  "*": lambda x, y: x * y,
# # # # # #                  "/": lambda x, y: int(x / y)}

# # # # # #     for token in tokens:
# # # # # #         if token in operators:
# # # # # #             y = stack.pop()
# # # # # #             x = stack.pop()
# # # # # #             operation = operators[token]
# # # # # #             result = operation(x, y)
# # # # # #             stack.append(result)
# # # # # #         else:
# # # # # #             stack.append(int(token))

# # # # # #     return stack[-1]

# # # # # # rpn_expression = ['1','2','3','+','4','5','6','*','-','7','*','+','-','8','9','*','+']
# # # # # # print(evalRPN(rpn_expression))

# # # # # # define a new type of exception for stack ADT
# # # # # # class Empty(Exception):
# # # # # #   ''' Error attempting to access an element from an empty container.'''
# # # # # #   pass

# # # # # # class ArrayStack:
# # # # # #   ''' LIFO stack implementation using a Python List as underlying storage'''

# # # # # #   def __init__(self):# constructor
# # # # # #     ''' create an empty stack'''
# # # # # #     self._data = []    # nonpublic list instance

# # # # # #   def __len__(self):
# # # # # #     ''' return the number of elements in a stack'''
# # # # # #     return len(self._data)

# # # # # #   def is_empty(self):
# # # # # #     ''' Return True if the stack is empty'''
# # # # # #     return len(self._data) == 0

# # # # # #   def push(self, e):
# # # # # #     ''' Add element e to the top of the stack'''
# # # # # #     self._data.append(e)  # new item stored at end of a list

# # # # # #   def top(self):
# # # # # #     '''
# # # # # #     Return the element at the top of the stack
# # # # # #     Raise Empty Exception if the stack is empty
# # # # # #     '''
# # # # # #     if self.is_empty():
# # # # # #       raise Empty('Stack is Empty')
# # # # # #     return self._data[-1]           # the last item in the list

# # # # # #   def pop(self):
# # # # # #     '''
# # # # # #     Remove and return the element from the top of the stack
# # # # # #     Raise Empty excepion if the stack is empty
# # # # # #     '''
# # # # # #     if self.is_empty():
# # # # # #       raise Empty('Stack is Empty')
# # # # # #     return self._data.pop()

# # # # # #   def __str__(self):
# # # # # #     '''
# # # # # #     A string representation of the stack
# # # # # #     An arrow shows the top of the stack
# # # # # #     '''
# # # # # #     return ''.join(str(self._data)) +'>'
  
# # # # # #   # Creating a stack
# # # # # # def create_stack():
# # # # # #     stack = []
# # # # # #     return stack


# # # # # # # Creating an empty stack
# # # # # # def check_empty(stack):
# # # # # #     return len(stack) == 0


# # # # # # # Adding items into the stack
# # # # # # def push(stack, item):
# # # # # #     stack.append(item)
# # # # # #     print("pushed item: " + item)


# # # # # # # Removing an element from the stack
# # # # # # def pop(stack):
# # # # # #     if (check_empty(stack)):
# # # # # #         return "stack is empty"

# # # # # #     return stack.pop()

# # # # # # # reversing data using a stack
# # # # # # def reverse_file(filename):
# # # # # #   ''' Overwrite given file with its conent line-by-line reversed'''

# # # # # #   S = ArrayStack()
# # # # # #   original = open(filename)
# # # # # #   for line in original:
# # # # # #     S.push(line.rstrip('\n')) # we will re-insert newlines when writing
# # # # # #   original.close()

# # # # # #   # Now we overwrite with contents in LIFO order
# # # # # #   output = open(filename, 'w') # reopening file overwrites original
# # # # # #   while not S.is_empty():
# # # # # #     output.write(S.pop() + '\n') # re-insert newline characters
# # # # # #   output.close()

# # # # # # ###########
# # # # # # file = open("initial.txt", 'w')
# # # # # # file.write("I am going home.\n")
# # # # # # file.write("Today is a holiday.")
# # # # # # file.close()

# # # # # # type initial.txt
# # # # # # print('\n\n')
# # # # # # reverse_file("initial.txt")
# # # # # # type initial.txt

# # # # # # import collections

# # # # # # D = collections.deque()
# # # # # # D.appendleft(15)
# # # # # # D.appendleft(12); D.append(66)
# # # # # # print(D)

# # # # # # from collections import deque

# # # # # # D = deque()
# # # # # # D.appendleft(55)
# # # # # # a = D.is_empty()
# # # # # # print(a)

# # # # # # class Empty(Exception):
# # # # # #   ''' Error attempting to access an element from an empty container.'''
# # # # # #   pass

# # # # # # class LinkedStack:

# # # # # #     # class Node:#nested class
# # # # # #     #     __slots__=['_element','_next']

# # # # # #     #     def __init__(self, element, next):
# # # # # #     #         self._element = element #노드의 데이터
# # # # # #     #         self._next = next #노드의 포인터
# # # # # #     class Node:
# # # # # #         def __init__(self,element,next):
# # # # # #             self._element = element
# # # # # #             self._next = next
    
# # # # # #     # def __init__(self):
# # # # # #     #     self._head = None #헤드 노드                  
# # # # # #     #     self._size = 0 #노드 개수

# # # # # #     def __init__(self):
# # # # # #         self._head = None
# # # # # #         self._size = 0


# # # # # #     # def __len__(self):
# # # # # #     #     return self._size
    
# # # # # #     def __len__(self):
# # # # # #         return self._size

# # # # # #     # def is_empty(self):
# # # # # #     #     return self._size == 0

# # # # # #     def is_empty(self):
# # # # # #         return self._size == 0
    

    
# # # # # #     # def top(self):
# # # # # #     #     if self.is_empty():
# # # # # #     #         raise Empty('Stack is Empty')
# # # # # #     #     return self._head._element

# # # # # #     def top(self):
# # # # # #         if self._size == 0:
# # # # # #             raise Empty('Stack is Empty')
# # # # # #         return self._head._element
    
# # # # # #     # def push(self,e): #push할떄 노드를 만든다. self가 S가 된다. nested 클래스를 속성처럼 쓰는 구나 여기서 self._head를 노드로 만들었으니 self._head._element이런식으로 쓸수 있다.
# # # # # #     #     self._head = self.Node(e,self._head)
# # # # # #     #     self._size += 1

# # # # # #     def push(self,e):
# # # # # #         self._head = self.Node(e,self._head)
# # # # # #         self._size += 1

# # # # # #     # def pop(self):
# # # # # #     #     if self.is_empty():
# # # # # #     #         raise Empty('Stack is Empty')
# # # # # #     #     answer = self._head._element
# # # # # #     #     self._head = self._head._next
# # # # # #     #     self._size -= 1
# # # # # #     #     return answer
    
# # # # # #     def pop(self):
# # # # # #         if self._size == 0:
# # # # # #             raise Empty('Stack is Empty')
# # # # # #         answer = self._head._element
# # # # # #         self._head = self._head._next
# # # # # #         self._size -= 1 
# # # # # #         return answer

# # # # # #     # def __str__(self):
# # # # # #     #     ''' String representation of the stack'''
# # # # # #     #     arr = ''
# # # # # #     #     start = self._head
# # # # # #     #     for i in range(self._size):
# # # # # #     #         arr += str(start._element) +', '
# # # # # #     #         start = start._next

# # # # # #     #     return '<' + arr + ']'

# # # # # #     def __str__(self):
# # # # # #         arr = ''
# # # # # #         start = self._head
# # # # # #         for i in range(self._size):
# # # # # #             arr += str(start._element) + ', '
# # # # # #             start = start._next
# # # # # #         return '<'+arr+']'
            
# # # # # # if __name__ == '__main__':

# # # # # #   S = LinkedStack()
# # # # # #   S.push(10)
# # # # # #   S.push(15)
# # # # # #   S.push(3)
# # # # # #   S.push(17)
# # # # # #   S.push(0)
# # # # # #   S.push(2)
# # # # # #   print('Stack Length: ', len(S))
# # # # # #   print('Stack S: ', S)

# # # # # #   print('Pop :', S.pop())
# # # # # #   print('Pop :', S.pop())

# # # # # #   print('Stack Length: ', len(S))
# # # # # #   print('Stack S: ', S)

# # # # # class Empty(Exception):
# # # # #   ''' Error attempting to access an element from an empty container.'''
# # # # #   pass

# # # # # class _DoublyLinkedBase:#부모클래스
# # # # #   '''A base class providing a doubly linked list representation.'''

# # # # #   #-----------------------------------------------------------------
# # # # # #   class _Node:
# # # # # #     '''Lightweight, nonpublic class for storing a doubly linked node.'''
# # # # # #     __slots__ = ['_element', '_prev', '_next']        # streamline memory

# # # # # #     def __init__(self, element, prev, next): # initialize node's field
# # # # # #       self._element = element       # element to be stored
# # # # # #       self._prev = prev             # Previous node reference
# # # # # #       self._next = next             # next node reference
# # # # #   # class _Node:
# # # # #   #   def __init__(self, element, prev, next):
# # # # #   #     self._element = element
# # # # #   #     self._prev = prev
# # # # #   #     self._next = next
# # # # #   class _Node:
# # # # #     def __init__(self, element, prev, next):
# # # # #       self._element = element
# # # # #       self._prev = prev
# # # # #       self._next = next
# # # # # #-------------------------------------------------------------------
# # # # # #   def __init__(self):
# # # # # #     '''Create an empty list.'''
# # # # # #     self._header = self._Node(None, None, None) #헤더랑 테일은 따로 만들지 않아도 자동으로 만들어지는 개념
# # # # # #     self._trailer = self._Node(None, None, None)
# # # # # #     self._header._next = self._trailer      # trailer is after header
# # # # # #     self._trailer._prev = self._header      # header is before trailer
# # # # # #     self._size = 0                          # Number of elements

# # # # #   def __init__(self):
# # # # #     self._header = self._Node(None, None, None)#헤더랑 테일은 없는걸 만드는 것이니 속석에 None들어가게 Node 만드는 것
# # # # #     self._trailer = self._Node(None, None, None)#header, trailer라는 변수에 노드를 할당한 것 즉 self._header를 이용하여 노드에 접근할 수 있다.
# # # # #     self._header._next = self._trailer
# # # # #     self._trailer._prev = self._header
# # # # #     self._size = 0
# # # # # #   def __len__(self):
# # # # # #     '''Return the number of elements in the list.'''
# # # # # #     return self._size
# # # # #   def __len__(self):
# # # # #     return self._size
  
# # # # # #   def is_empty(self):
# # # # # #     '''Return True if list is empty.'''
# # # # # #     return self._size == 0
# # # # #   def is_empty(self):
# # # # #     return self._size == 0
  
# # # # # #   def _insert_between(self, e, predecessor, successor):                                           #노드를 인수로 받는다.
# # # # # #     '''Add element e between two existing nodes and return new node.'''
# # # # # #     newest = self._Node(e, predecessor, successor) # linked to neighbors
# # # # # #     predecessor._next = newest
# # # # # #     successor._prev = newest
# # # # # #     self._size += 1
# # # # # #     return newest
# # # # # # def _insert_between(self, e, predecessor, successor):                                             #newest노드의 next와 prev는 Node 클래스를 통해 이미 할당되었다.
# # # # # #   newest = self._Node(e, predecessor, successor)
# # # # # #   predecessor._next = newest
# # # # # #   successor._prev = newest
# # # # # #   self._size += 1
# # # # # #   return newest
# # # # #   def _insert_between(self, e, predecessor, successor):                                             #노드의 다리는 연결했으니 앞, 뒤 노드의 다리를 이 노드에 연결해야한다.
# # # # #     newest = self._Node(e, predecessor, successor)
# # # # #     predecessor._next = newest
# # # # #     successor._prev = newest
# # # # #     self._size += 1
# # # # #     return newest                                                                                   #노드를 리턴한다.
  
# # # # #   def _delete_node(self, node):
# # # # #     '''Delete nonsentinel node from the list and return its element.'''
# # # # #     predecessor = node._prev
# # # # #     successor = node._next
# # # # #     predecessor._next = successor
# # # # #     successor._prev = predecessor
# # # # #     self._size -= 1                 # record deleted element
# # # # #     element = node._element
# # # # #     node._prev = node._next = node._element = None # deprecate node
# # # # #     return element      # return deleted element

# # # # #   # def _delete_node(self, node):
# # # # #   #   node._prev._next = node._next
# # # # #   #   node._next._prev = node._prev
# # # # #   #   element = node._element
# # # # #   #   node._next = None
# # # # #   #   node._prev = None
# # # # #   #   node._element = None
# # # # #   #   self._size -= 1
# # # # #   #   return element

# # # # # ############################################################################
# # # # # class LinkedDeque(_DoublyLinkedBase):         # note the use of inheritance 자식클래스
# # # # #   '''Double-ended queue implementation based on a doubly linked list.'''

# # # # #   def first(self):
# # # # #     '''Return (but do not remove) the element at the front of the deque.'''
# # # # #     if self.is_empty():
# # # # #       raise Empty("Deque is empty")
# # # # #     return self._header._next._element      # real item just after header

# # # # #   def last(self):
# # # # #     '''Return (but do not remove) the element at the back of the deque.'''
# # # # #     if self.is_empty():
# # # # #       raise Empty("Deque is empty")
# # # # #     return self._trailer._prev._element     # real item just before trailer

# # # # #   def insert_first(self, e):
# # # # #     '''Add an element to the front of the deque.'''
# # # # #     self._insert_between(e, self._header, self._header._next) # after header

# # # # #   def insert_last(self, e):
# # # # #     '''Add an element to the back of the deque.'''
# # # # #     self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

# # # # #   def delete_first(self):
# # # # #     '''
# # # # #     Remove and return the element from the front of the deque.
# # # # #     Raise Empty exception if the deque is empty.
# # # # #     '''
# # # # #     if self.is_empty():
# # # # #       raise Empty("Deque is empty")
# # # # #     return self._delete_node(self._header._next) # use inherited method 

# # # # #   def delete_last(self):
# # # # #     '''
# # # # #     Remove and return the element from the back of the deque.
# # # # #     Raise Empty exception if the deque is empty.
# # # # #     '''
# # # # #     if self.is_empty():
# # # # #       raise Empty("Deque is empty")
# # # # #     return self._delete_node(self._trailer._prev)  # use inherited method

# # # # # #   def __str__(self):
# # # # # #     ''' String representation of deque '''

# # # # # #     arr = ''
# # # # # #     start = self._header._next
# # # # # #     for i in range(self._size):
# # # # # #       arr += str(start._element) + ', '
# # # # # #       start = start._next
# # # # # #     return '<' + arr + '>'

# # # # # # def __str__(self):
# # # # # #   arr = ''
# # # # # #   start = self._header._next
# # # # # #   for i in range(self._size):
# # # # # #     arr = arr + str(start._element) + ', '
# # # # # #     start = start._next
# # # # # #   return '<'+arr+'>'

# # # # #   def __str__(self):
# # # # #     arr = ''
# # # # #     start = self._header._next
# # # # #     for i in range(self._size):
# # # # #       arr += str(start._element) + ', '
# # # # #       start = start._next
# # # # #     return '<'+arr+'>'


# # # # # ##############

# # # # # # D = LinkedDeque()
# # # # # # D.insert_first(10)
# # # # # # D.insert_first(15)
# # # # # # D.insert_last(5)
# # # # # # D.insert_last(-1)
# # # # # # D.insert_first(20)

# # # # # # print('Length of Deque: ', len(D))
# # # # # # print('D: ', D)

# # # # # # print('Delete from head: ', D.delete_first())
# # # # # # print('Delete from tail ', D.delete_last())


# # # # # # print('Length of Deque: ', len(D))
# # # # # # print('D: ', D)

# # # # # #Execute the cell containing _DoublyLinkedBase Class before running this cell

# # # # # class PositionalList(_DoublyLinkedBase):
# # # # #   '''A sequential container of elements allowing positional access'''

# # # # #   # class _Node: 노드는 이런식으로 nested class로 구현
# # # # #   #   def __init__(self, element, prev, next):
# # # # #   #     self._element = element
# # # # #   #     self._prev = prev
# # # # #   #     self._next = next 

# # # # #   # -------------- nested Position Class ----------------------------
# # # # #   class Position:
# # # # #     '''An abstraction representing the location of a single element'''

# # # # #     # def __init__(self, container, node):
# # # # #     #   '''Constructor should not be invoked by user'''
# # # # #     #   self._container = container
# # # # #     #   self._node = node
# # # # #     # def __init__(self, container, node):
# # # # #     #   self._container = container
# # # # #     #   self._node = node
# # # # #     def __init__(self, container, node):
# # # # #       self._container = container
# # # # #       self._node = node                                        #포지션의 노드를 표현할 때 사용
# # # # #     # def element(self):
# # # # #     #   '''Return the element stored at this Position'''
# # # # #     #   return self._node._element
# # # # #     def element(self):#포지션의 원소 출력
# # # # #       return self._node._element
    
# # # # #     def __eq__(self, other):
# # # # #       '''Return True if other is a Position representing the same location'''
# # # # #       return type(other) is type(self) and other._node is self._node

# # # # #     def __ne__(self, other):
# # # # #       '''Return True if other does not represent the same location'''
# # # # #       return not (self == other)
    
# # # # #   #-------------------- Utility Methods ---------------------------
# # # # #   #position이 가리키는 노드 리턴
# # # # #   def _validate(self, p):
# # # # #     '''Return position's node or raise appropriate error if invalid'''
# # # # #     if not isinstance(p, self.Position): # p 가 Position의 객체인지 판별하는 것
# # # # #       raise TypeError('p must be proper Position type')
# # # # #     if p._container is not self:
# # # # #       raise ValueError('p does not belong to this container')
# # # # #     if p._node._next is None:   # convention for depricated nodes
# # # # #       raise ValueError('p is no longer valid')
# # # # #     return p._node
# # # # # #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# # # # #   def _make_position(self, node):                                                       #여기서 인수로 받는 node의 position 객체를 만들어서 리턴한다..
# # # # #     ''' Return Position instance for a given node(or None if sentinel)'''
# # # # #     if node is self._header or node is self._trailer:                                   #header와 trailer에 대해선 position안 만든다는 것
# # # # #       return None             #boundary violation - sentinel node
# # # # #     else:
# # # # #       return self.Position(self, node)    # legitimate position                         #해당 노드가 header나 trailer가 아니면 position 객체 만든다.
    
# # # # #   # ------------------- 노드에 직접 접근하는 접근자 Accessors ----------------------------
# # # # #   def first(self):#젤 앞 포지션 리턴
# # # # #     ''' Return the first Position in the list (or None if list is empty)'''
# # # # #     return self._make_position(self._header._next)

# # # # #   def last(self):#젤 끝 포지션 리턴
# # # # #     '''Return the last Position in the list (or None if list is empty)'''
# # # # #     return self._make_position(self._trailer._prev)

# # # # #   def before(self, p):#현재 포지션의 앞 포지션 리턴
# # # # #     '''Return the Position just before Position p (or None if p is first)'''
# # # # #     node = self._validate(p)#포지션이 가리키는 노드 리턴
# # # # #     return self._make_position(node._prev)

# # # # #   def after(self, p):#현재 포지션의 뒷 포지션 리턴
# # # # #     '''Return the Position just after Position p (or None if p is last)'''
# # # # #     node = self._validate(p)#포지션이 가리키는 노드 리턴
# # # # #     return self._make_position(node._next)

# # # # #   def __iter__(self):
# # # # #     '''Generate a forward iteration of the elements of the list'''
# # # # #     cursor = self.first()#커서는 포지션
# # # # #     while cursor is not None:
# # # # #       yield cursor.element()
# # # # #       cursor = self.after(cursor)

# # # # #   def __str__(self):
# # # # #     ''' Generates a string representation of the list'''
# # # # #     # arr = ''
# # # # #     # cursor = self.first()                                                   #여기서의 self 는 positional list이다. 그렇기에 first() 사용 가능하다.
# # # # #     # while cursor is not None:
# # # # #     #   arr += str(cursor.element()) + ', '
# # # # #     #   cursor = self.after(cursor)                                           #마지막 포지션이면 after메서드 통과시 포지션이 None이 된다.
# # # # #     # return '<' + arr + '>'                                                  
# # # # #     arr = ''
# # # # #     cursor = self.first()                                                     #cursor는 처음으로 header 노드 바로 뒷 노드의 포지션을 할당받는다.
# # # # #     while cursor is not None:                                                 #포지션 객체는 position 클래스의 속성을 가질 수 있다. p._node 이런식으로
# # # # #       arr += str(cursor.element()) + ', '
# # # # #       cursor = self.after(cursor)                                             #cursor는 position 클래스의 객체이니 after 메서드 사용 X 그래서 self로 사용
# # # # #     return '<' + arr + '>'

# # # # #   #-------------- Mutators ------------------------------                     #return으로 다 포지션 객체 리턴
# # # # #   # override inherited version to return Position, rather than Node
# # # # #   # def _insert_between(self, e, predecessor, successor):
# # # # #   #   '''Add element between existing nodes and return new Position'''
# # # # #   #   node = super()._insert_between(e, predecessor, successor)
# # # # #   #   return self._make_position(node)
# # # # #   def _insert_between(self, e, predecessor, successor):                       #delete 말고는 다 인수로 element 받는다. 즉 노드를 포지션을 통해 삽입하는 것이니...
# # # # #     node = super()._insert_between(e, predecessor, successor)                 #DoubleLinkedList 클래스에 있는 insert함수에서 self.Node()를 토해서 노드를 만들고 그 노드를 할당
# # # # #     return self._make_position(node)
  
# # # # #   def add_first(self, e):
# # # # #     '''Insert element e at the front of the list and return new Position'''
# # # # #     return self._insert_between(e, self._header, self._header._next)

# # # # #   def add_last(self, e):
# # # # #     '''Insert element e at the back of the list and return new Position'''
# # # # #     return self._insert_between(e, self._trailer._prev, self._trailer)

# # # # #   def add_before(self, p, e):                                                              #위에 add_first, add_last는 헤더와 트레일러 노드를 기준으로 하면되기에 포지션을 인수로 안 받아도 된다.
# # # # #     '''Insert element e into list before Position p and return new Position'''
# # # # #     original = self._validate(p)                                                           #인수로 받은 포지션의 노드를 orginal에 할당
# # # # #     return self._insert_between(e, original._prev, original)

# # # # #   def add_after(self, p, e):
# # # # #     '''Insert element e into list after Position p and return new Position.'''
# # # # #     original = self._validate(p)
# # # # #     return self._insert_between(e, original, original._next)

# # # # #   def delete(self, p):
# # # # #     '''Remove and return the element at Position p'''
# # # # #     original = self._validate(p)
# # # # #     return self._delete_node(original) # inherited method returns element                 #리턴으로 노드의 element 반환

# # # # #   def replace(self, p, e):                                                                #포지션을 통해 들어간 노드의 element를 바꾸는 메서드 old_value를 반환
# # # # #     '''
# # # # #     Replace the element at Position p with e.
# # # # #     Return the element formerly at Position p.
# # # # #     '''
# # # # #     original = self._validate(p)
# # # # #     old_value = original._element
# # # # #     original._element = e
# # # # #     return old_value

# # # # # ################################

# # # # # L = PositionalList()
# # # # # L.add_first(5)
# # # # # L.add_last(10)
# # # # # L.add_first(7)
# # # # # L.add_first(-2)
# # # # # L.add_last(3)

# # # # # print('Length of List: ', len(L))
# # # # # print('Positional List: ', L)

# # # # # print('Delete: ', L.delete(L.first()))
# # # # # print('Delete: ', L.delete(L.last()))

# # # # # print('Length of List: ', len(L))
# # # # # print('Positional List: ', L)

# # # # # L.add_before(L.last(), 11)
# # # # # L.add_after(L.first(), 15)

# # # # # print('Length of List: ', len(L))
# # # # # print('Positional List: ', L)

# # # # # L.replace(L.last(), 1)
# # # # # L.replace(L.after(L.first()), 100) # Second position

# # # # # print('Length of List: ', len(L))
# # # # # print('Positional List: ', L)

# # # # # print("Using Iterator to print elements:")
# # # # # for e in L:
# # # # #   print(e, end=' ')

# # # # # def insertion_sort(L):
# # # # #   if len(L) > 1:
# # # # #     marker = L.first()
# # # # #     while marker != L.last():
# # # # #       pivot = L.after(marker)
# # # # #       value = pivot.element()
# # # # #       if value > marker.element():
# # # # #         marker = pivot
# # # # #       else:
# # # # #         walk = marker
# # # # #         while walk != L.first() and L.before(walk).element() > value:
# # # # #           walk = L.before(walk)
# # # # #         L.delete(pivot)
# # # # #         L.add_before(walk, value)
# # # # # insertion_sort(L)
# # # # # print(L)

# # # # # # Execute the cells containing the PositionList / _DoublyLinkedBase above
# # # # # # Before running this cell

# # # # # class FavoritesList:
# # # # #   '''List of elements ordered from most frequently accessed to least.'''

# # # # #   #------------------- nested _Item Class ------------------------
# # # # #   class _Item:
# # # # #     __slots__ = '_value', '_count'       # streamline memory usage

# # # # #     def __init__(self, e):
# # # # #       self._value = e                     # user's element
# # # # #       self._count = 0                     # access count initially 0

# # # # #   #----------------- non-public utilities ----------------------------
# # # # #   def _find_position(self, e):
# # # # #     '''Search for element e and return its Position (or None if not found)'''
# # # # #     walk = self._data.first()                                                                       #positionalList 객체에 first() 적용
# # # # #     while walk is not None and walk.element()._value != e:
# # # # #       walk = self._data.after(walk)  # move forward
# # # # #     return walk

# # # # #   def _move_up(self, p):
# # # # #     '''Move item at Position p earlier in the list based on access count'''
# # # # #     if p != self._data.first(): # otherwise, already at top, can't move up
# # # # #       cnt = p.element()._count
# # # # #       walk = self._data.before(p) # move up
# # # # #       if cnt > walk.element()._count:
# # # # #         while (walk != self._data.first() and
# # # # #                cnt > self._data.before(walk).element()._count):
# # # # #           walk = self._data.before(walk) # keep moving upward
# # # # #         self._data.add_before(walk, self._data.delete(p)) # delete / reinsert


# # # # #   # ----------------- Public Methods --------------------------------
# # # # #   def __init__(self):                                                                               #positionalList 객체 만들어서 할당
# # # # #     ''' Create an empty list of favourites'''
# # # # #     self._data = PositionalList()       # will be a list of _Item instances

# # # # #   def __len__(self):
# # # # #     '''Return the number of entries on the favourite list'''
# # # # #     return len(self._data)

# # # # #   def is_empty(self):
# # # # #     '''Return True if list is empty.'''
# # # # #     return len(self._data == 0)

# # # # #   def access(self, e):
# # # # #     '''Access element e, thereby increasing its access count'''
# # # # #     p = self._find_position(e)  # try to locate the existing element
# # # # #     if p is None:
# # # # #       p = self._data.add_last(self._Item(e))  # if new, place at end
# # # # #     p.element()._count += 1       # increment its access count
# # # # #     self._move_up(p)              # consider moving forward

# # # # #   def remove(self, e):
# # # # #     ''' Remove element e from the list of favourites'''
# # # # #     p = self._find_position(e)    # locate existing element
# # # # #     if p is not None:
# # # # #       self._data.delete(p)        # delete if found

# # # # #   def top(self, k):
# # # # #     '''Generate a sequence of top k elements in terms of access count.'''
# # # # #     if not 1 <= k <= len(self):
# # # # #       raise ValueError('Illegal value for k')
# # # # #     walk = self._data.first()
# # # # #     for j in range(k):
# # # # #       item = walk.element()       # element of list is _Item
# # # # #       yield item._value           # report user's element
# # # # #       walk = self._data.after(walk) # move forward


# # # # # ####################

# # # # # F = FavoritesList()
# # # # # F.access('BackStreetBoys')
# # # # # F.access('KatyPerry')
# # # # # F.access('Eminem')
# # # # # F.access('MichaelJackson')
# # # # # F.access('ImagineDragons')
# # # # # F.access('BritneySpears')
# # # # # F.access('BackStreetBoys')
# # # # # F.access('ImagineDragons')
# # # # # F.access('ImagineDragons')
# # # # # F.access('ImagineDragons')
# # # # # F.access('KatyPerry')
# # # # # F.access('Eminem')


# # # # # for k in F.top(5):
# # # # #   print(k)


# # # # # F.access('BritneySpears')
# # # # # F.access('BritneySpears')
# # # # # F.access('BritneySpears')
# # # # # F.access('BritneySpears')
# # # # # F.access('BritneySpears')

# # # # # print('\nUpdated Favourites \n')
# # # # # for k in F.top(5):
# # # # #   print(k)

# # # # def draw_line(tick_length, tick_label=''):
# # # #   '''
# # # #   Draw one line with given tick length (followed by optional label)
# # # #   '''
# # # #   line = '_'*tick_length
# # # #   if tick_label:
# # # #     line += ' ' + tick_label
# # # #   print(line)

# # # # def draw_interval(center_length):
# # # #   '''
# # # #   Draw tick interval based upon a central tick length
# # # #   '''
# # # #   if center_length > 0:  # stop when length drops to 0
# # # #     draw_interval(center_length - 1) # recursively draw top tics
# # # #     draw_line(center_length) # draw center tick
# # # #     draw_interval(center_length - 1) # recursively draw bottom ticks

# # # # def draw_ruler(num_inches, major_length):
# # # #   '''
# # # #   Draw English ruler with given number of inches, major tick length
# # # #   '''
# # # #   draw_line(major_length, '0')     # draw inch 0 line
# # # #   for j in range(1, 1+num_inches):
# # # #     draw_interval(major_length - 1)  # draw interior ticks for inch
# # # #     draw_line(major_length, str(j))  # draw nch j line and label

# # # # draw_ruler(2, 2)
# # # # # draw_ruler(2,3)
# # # # # draw_ruler(2,5)

# # # # Binary Search algorithm through recursion

# # # def binary_search(data, target, low, high):                                                          #인덱스가 인수
# # #   '''
# # #   Return True if target is found in the indicated interval [low, high]
# # #   '''
# # #   if low > high:
# # #     return False  # interval is empty, no match found
# # #   else:
# # #     mid = (low + high) // 2                                                                          #인덱스를 할당
# # #     if target == data[mid]:
# # #       return mid, True # Match found
# # #     elif target < data[mid]:
# # #       # recur on the first half of the interval
# # #       return binary_search(data, target, low, mid-1)
# # #     else:
# # #       # recur on the second half of the interval
# # #       return binary_search(data, target, mid+1, high)
# # #       #return binary_search(data, target, mid, high) # leads to infinite recursion


# # # a = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]                                        #정렬된 리스트

# # # print(binary_search(a, 22, 0, 15))

# # # Element uniqueness problem
# # # def unique3(S, start, stop):                                                                        #중복된 원소 있으면 False 없으면 True
# # #   '''
# # #   Return True if there is no duplicate elements in the array
# # #   '''
# # #   if stop - start <= 1: return True  # at most one item                                             #o(1)의 시간복잡도 가짐
# # #   elif not unique3(S, start, stop-1): return False # first part has duplicate
# # #   elif not unique3(S, start+1, stop): return False # second part has duplicate
# # #   else: return S[start] != S[stop-1] # do first and last differ


# # # a = [2,23,1,3,4]
# # # print(a[0:5])
# # # print(unique3(a, 0, 2))

# # # def depth(self, p):
# # #     if self.is_root(p):
# # #         return 0
# # #     else:
# # #         return 1 + self.depth(self.parent(p))

# # # class TreeNode:
# # #     def __init__(self, val=0, left=None, right=None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right

# # # def preorderTraversal(root):
# # #     if root is None:
# # #         return
# # #     print(root.val)  # 현재 노드 방문
# # #     preorderTraversal(root.left)  # 왼쪽 서브트리 순회
# # #     preorderTraversal(root.right)  # 오른쪽 서브트리 순회

# # # # Example usage:
# # # # 이진 트리 생성
# # # #       1
# # # #      / \
# # # #     2   3
# # # #    / \
# # # #   4   5
# # # root = TreeNode(1)
# # # root.left = TreeNode(2)
# # # root.right = TreeNode(3)
# # # root.left.left = TreeNode(4)
# # # root.left.right = TreeNode(5)

# # # # 전위 순회 호출
# # # print("Preorder traversal:")
# # # preorderTraversal(root)


# # # Execute the cells containing the PositionList / _DoublyLinkedBase above
# # # Before running this cell

# # class FavoritesList:
# #   '''List of elements ordered from most frequently accessed to least.'''

# #   #------------------- nested _Item Class ------------------------
# #   class _Item:
# #     __slots__ = '_value', '_count'       # streamline memory usage

# #     def __init__(self, e):
# #       self._value = e                     # user's element
# #       self._count = 0                     # access count initially 0

# #   #----------------- non-public utilities ----------------------------
# #   def _find_position(self, e):
# #     '''Search for element e and return its Position (or None if not found)'''
# #     walk = self._data.first()
# #     while walk is not None and walk.element()._value != e:
# #       walk = self._data.after(walk)  # move forward
# #     return walk

# #   def _move_up(self, p):
# #     '''Move item at Position p earlier in the list based on access count'''
# #     if p != self._data.first(): # otherwise, already at top, can't move up
# #       cnt = p.element()._count
# #       walk = self._data.before(p) # move up
# #       if cnt > walk.element()._count:
# #         while (walk != self._data.first() and
# #                cnt > self._data.before(walk).element()._count):
# #           walk = self._data.before(walk) # keep moving upward
# #         self._data.add_before(walk, self._data.delete(p)) # delete / reinsert


# #   # ----------------- Public Methods --------------------------------
# #   def __init__(self):
# #     ''' Create an empty list of favourites'''
# #     self._data = PositionalList()       # will be a list of _Item instances

# #   def __len__(self):
# #     '''Return the number of entries on the favourite list'''
# #     return len(self._data)

# #   def is_empty(self):
# #     '''Return True if list is empty.'''
# #     return len(self._data == 0)

# #   def access(self, e):
# #     '''Access element e, thereby increasing its access count'''
# #     p = self._find_position(e)  # try to locate the existing element
# #     if p is None:
# #       p = self._data.add_last(self._Item(e))  # if new, place at end
# #     p.element()._count += 1       # increment its access count
# #     self._move_up(p)              # consider moving forward

# #   def remove(self, e):
# #     ''' Remove element e from the list of favourites'''
# #     p = self._find_position(e)    # locate existing element
# #     if p is not None:
# #       self._data.delete(p)        # delete if found

# #   def top(self, k):
# #     '''Generate a sequence of top k elements in terms of access count.'''
# #     if not 1 <= k <= len(self):
# #       raise ValueError('Illegal value for k')
# #     walk = self._data.first()
# #     for j in range(k):
# #       item = walk.element()       # element of list is _Item
# #       yield item._value           # report user's element
# #       walk = self._data.after(walk) # move forward


# # ####################

# # F = FavoritesList()
# # F.access('BackStreetBoys')
# # F.access('KatyPerry')
# # F.access('Eminem')
# # F.access('MichaelJackson')
# # F.access('ImagineDragons')
# # F.access('BritneySpears')
# # F.access('BackStreetBoys')
# # F.access('ImagineDragons')
# # F.access('ImagineDragons')
# # F.access('ImagineDragons')
# # F.access('KatyPerry')
# # F.access('Eminem')


# # for k in F.top(5):
# #   print(k)


# # F.access('BritneySpears')
# # F.access('BritneySpears')
# # F.access('BritneySpears')
# # F.access('BritneySpears')
# # F.access('BritneySpears')

# # print('\nUpdated Favourites \n')
# # for k in F.top(5):
# #   print(k)

# #from IPython.core.debugger import set_trace

# # Linked Binary tree

# class Tree:
#   '''Abstract Base Class representing a tree structure'''

#   # --------- Nested Position Class -----------
#   class Position:
#     '''An abstraction representing the location of a single element'''

#     def element(self):
#       '''return the element stored at this position'''
#       raise NotImplementedError('must be implemented by subclass')

#     def __eq__(self, other):
#       '''Return True if other Position represents the same location'''
#       raise NotImplementedError('must be implemented by subclass')

#     def __ne__(self, other):
#       '''Return True if the other does not represent the same location.'''
#       return not(self == other)

#     #------------ Abstract Methods that concrete subclass must support ----

#   def root(self):
#     ''' Returns Position representing the tree's root (or None if Empty)'''
#     raise NotImplementedError('must be implemented by subclass')

#   def parent(self, p):
#     ''' Returns Position representing p's parent (or None if Empty)'''
#     raise NotImplementedError('must be implemented by subclass')

#   def num_children(self, p):
#     '''Return the number of children that Position p has.'''
#     raise NotImplementedError( 'must be implemented by subclass' )

#   def children(self, p):
#     '''Return the number of children that Position p has.'''
#     raise NotImplementedError( 'must be implemented by subclass' )

#   def __len__(self):
#     '''Return the total number of elements in the tree.'''
#     raise NotImplementedError( 'must be implemented by subclass' )

#     # ---------- concrete methods implemented in this class ----------

#   def is_root(self, p):
#     '''Return True if Position p represents the root of the tree.'''
#     return self.root() == p

#   def is_leaf(self, p):
#     '''Return True if Position p does not have any children.'''
#     return self.num_children(p) == 0

#   def is_empty(self):
#     '''Return True if the tree is empty.'''
#     return len(self) == 0

#   def depth(self, p):
#     '''
#     Return the number of levels
#     separating Position p from the root.
#     '''
#     if self.is_root(p):
#       return 0
#     else:
#       return 1 + self.depth(self.parent(p))

#   def _height1(self):
#     '''
#     Return the height of the tree
#     works but O(n^2) worst-case time
#     '''
#     return(max(self.depth(p)
#       for p in self.positions() if self.is_leaf(p)))

#   def _height2(self, p):
#     '''
#     Return the height of the tree
#     time is linear in size of sub-tree
#     '''
#     if self.is_leaf(p):
#       return 0
#     else:
#       return 1 + max(self._height2(c) for c in self.children(p))

#   def height(self, p = None):
#     '''
#     Return the height of subtree rooted at Position P
#     if p is None, return the height of the entire tree.
#     '''
#     if p is None:
#       p = self.root()
#     return self._height2(p)   # start _height2 recursion

#   def __iter__(self):
#     '''Generate an iteration of tree's elements'''
#     for p in self.positions():    # use same order as positions
#       yield p.element()           # but yield each element

#   def preorder(self):
#     '''Generate a preorder iteration of positions in the tree.'''
#     if not self.is_empty():
#       for p in self._subtree_preorder(self.root()):    # start recursion
#         yield p

#   def _subtree_preorder(self, p):
#     '''Generate a preorder iteration of positions in subtree rooted at p.'''
#     yield p                 # visit p before its subtrees
#     for c in self.children(p):    # for each child c
#       for other in self._subtree_preorder(c): # do preorder of c's subtree
#         yield other         # yield each element

#   def positions(self):
#     '''Generate an iteration of the tree's positions.'''
#     return self.preorder()        # return entire preorder iteration

#   def postorder(self):
#     '''Generate post order iteration of positions in the tree.'''
#     if not self.is_empty():
#       for p in self._subtree_postorder(self.root()):  # start recursion
#         yield p

#   def _subtree_postorder(self, p):
#     '''Generate a postorder iteration of positions in subtree rooted at p.'''
#     for c in self.children(p):        # for each child c
#       for other in self._subtree_postorder(c):  # do postorder of c's subtree
#         yield other                             # yield each element
#     yield p           # then visit p after visiting sub-trees.

#   def breadthfirst(self):
#     '''Generate a breadth-first iteration of the positions of the tree.'''
#     if not self.is_empty():
#       fringe = LinkedQueue()        # known positions not yet yielded
#       fringe.enqueue(self.root())   # store in queue starting with root
#       while not fringe.is_empty():
#         p = fringe.dequeue()        # remove from front of the queue
#         yield p                     # report this position
#         for c in self.children(p):
#           fringe.enqueue(c)         # add children to back of queue

# class BinaryTree(Tree):
#   '''Abstract base class representing a binary tree structure.'''

#   # -------- additional abstract methods --------------
#   def left(self, p):
#     '''
#     Return a Position representing p's left child.
#     Return None if p does not have a left child.
#     '''
#     raise NotImplementedError('Must be implemented by subclass')

#   def right(self, p):
#     '''
#     Return a Position representing p's right child.
#     Return None if p does not have a right child
#     '''
#     raise NotImplementedError('Must be implemented by subclass')

#   # ---------- concrete methods implemented in this class ----------

#   def sibling(self, p):
#     '''Return a Position representing p's sibling (or None if no sibling).'''
#     parent = self.parent(p)
#     if parent is None:            # p must be the root
#       return None                 # root has no sibling
#     else:
#       if p == self.left(parent):
#         return self.right(parent)   # possibly None
#       else:
#         return self.left(parent)    # possibly None


#   def children(self, p):
#     ''' Generate an iteration of Positions representing p's children'''
#     if self.left(p) is not None:
#       yield self.left(p)
#     if self.right(p) is not None:
#       yield self.right(p)

#   def inorder(self):  # inorder traversal is applicable only to Binary trees
#     '''Generate an inorder iteration of positions in the tree.'''
#     for p in self._subtree_inorder(self.root()):
#       yield p

#   def _subtree_inorder(self, p):
#     '''Generate an inorder iteration of positions in subtree rooted at p.'''
#     if self.left(p) is not None:    # if left child exists, traverse its subtree
#       for other in self._subtree_inorder(self.left(p)):
#         yield other
#     yield p                 # visit p between its subtrees
#     if self.right(p) is not None:   # if right child exists, traverse its subtree
#       for other in self._subtree_inorder(self.right(p)):
#         yield other

#   # override inherited version to make inorder the default
#   def positions(self):
#     '''Generate iteration of the tree's positions.'''
#     return self.inorder()       # make inorder the default traversal algorithm

# class LinkedBinaryTree(BinaryTree):
#   '''Linked representation of a binary tree structure.'''

#   class _Node:
#     __slots__='_element', '_parent','_left', '_right'
#     def __init__(self, element, parent=None, left=None, right=None):
#       self._element = element
#       self._parent = parent
#       self._left = left
#       self._right = right

#   class Position(BinaryTree.Position):
#     '''An abstraction representing the location of a single element.'''

#     def __init__(self, container, node):
#       '''Constructor should not be invoked by user.'''
#       self._container = container
#       self._node = node

#     def element(self):
#       '''Return the element stored at this position.'''
#       return self._node._element

#     def __eq__(self, other):
#       '''Return True if other is a position representing the same location.'''
#       return type(other) is type(self) and other._node is self._node

#   # ---------- hidden utility functions for LinkedBinary Tree ----
#   def _validate(self, p):
#     '''Return associated node, if position is valid.'''
#     if not isinstance(p, self.Position):
#       raise TypeError('p must be proper Position type')
#     if p._container is not self:
#       raise ValueError('p does not belong to this container')
#     if p._node._parent is p._node:  # convention for deprecated nodes
#       raise ValueError('p is no longer valid')
#     return p._node

#   def _make_position(self, node):
#     '''Return Position instance for a given node (or None if no node)'''
#     return self.Position(self, node) if node is not None else None

#   #-------- binary tree constructor -------------------------------
#   def __init__(self):
#     '''Create an initially empty binary tree'''
#     self._root = None
#     self._size = 0

#   # ----------- Public Accessors ------------------------------
#   def __len__(self):
#     '''Return the total number of elements in the tree.'''
#     return self._size

#   def root(self):
#     '''Return the root Position of the tree (or None if tree is empty).'''
#     return self._make_position(self._root)

#   def parent(self, p):
#     '''return the position P's parent (or None if p is root)'''
#     node = self._validate(p)
#     return self._make_position(node._parent)

#   def left(self, p):
#     '''Return the Position P's left child (or None if no left child).'''
#     node = self._validate(p)
#     return self._make_position(node._left)

#   def right(self, p):
#     '''Return the Position P's right child (or None if no right child).'''
#     node = self._validate(p)
#     return self._make_position(node._right)

#   def num_children(self, p):
#     '''Return the number of children of Position P.'''
#     node = self._validate(p)
#     count = 0
#     if node._left is not None:      # left child exists
#       count += 1
#     if node._right is not None:     # right child exists
#       count += 1
#     return count

#   def _print_children(self, p, arr):
#     if p is not None:
#       arr += str(p.element())+': '
#       if self.num_children(p) > 0:
#         for c in self.children(p):
#           arr += str(c.element()) + '\t'
#         arr += '\n'
#         for c in self.children(p):
#           arr = self._print_children(c, arr)
#       arr += '\n'
#     return arr

#   def __str__(self):
#     ''' Provide a string representation of the tree'''

#     start = self.root()
#     arr = ''
#     arr = self._print_children(start, arr)
#     return arr

#   # ----------- NonPublic tree update Methods ---------------------------------------
#   def _add_root(self, e):
#     '''
#     Place element e at the root of an empty tree and return new Position.
#     Raise ValueError if tree nonempty.
#     '''
#     if self._root is not None:  raise ValueError('Root Exists.')
#     self._size = 1
#     self._root = self._Node(e)
#     return self._make_position(self._root)

#   def _add_left(self, p, e):
#     '''
#     Create a new left child for Position P, storing element e.
#     Return the position of a new node.
#     Raise ValueError if Position p is invalid or p already has a left child.
#     '''
#     node = self._validate(p)
#     if node._left is not None: raise ValueError('Left child exists')
#     self._size += 1
#     node._left = self._Node(e, node) # node is its parent
#     return self._make_position(node._left)

#   def _add_right(self, p, e):
#     '''
#     Create a new right child for Position p, storing element e.
#     Return the position of new node.
#     Raise ValueError if Position p is invalid or p already has a right child.
#     '''
#     node = self._validate(p)
#     if node._right is not None: raise ValueError('Right Child Exists')
#     self._size += 1
#     node._right = self._Node(e, node)  # node is its parent
#     return self._make_position(node._right)

#   def _replace(self, p, e):
#     ''' replace the element at position P with e and return the old element.'''
#     node = self._validate(p)
#     old = node._element
#     node._element = e
#     return old

#   def _delete(self, p):
#     '''
#     Delete the node at Position p, and replace it with its child, if any.
#     Return the element that had been stored at Position p.
#     Raise ValueError if Position p is invalid or p has two children.
#     '''
#     node = self._validate(p)
#     if self.num_children(p) == 2: raise ValueError('p has two children')
#     child = node._left if node._left else node._right
#     if child is not None:
#       child._parent = node._parent   # child's grandparent becomes parent
#     if node is self._root:
#       self._root = child        # child becomes root if its parent is deleted
#     else:
#       parent = node._parent
#       if node is parent._left:
#         parent._left = child
#       else:
#         parent._right = child
#     self._size -= 1
#     node._parent = node             # convention for deprecated node
#     return node._element

#   def _attach(self, p, t1, t2):
#     '''Attach trees t1 and t2 as left and right subtrees of external p.'''

#     node = self._validate(p)

#     if not self.is_leaf(p): raise ValueError('position must be leaf')
#     if not type(self) is type(t1) is type(t2): # all 3 tree must be same type
#       raise TypeError('Tree types must match')
#     self._size += len(t1) + len(t2)

#     if not t1.is_empty():  # attach t1 as left subtree of node
#       t1._root._parent = node
#       node._left = t1._root
#       t1._root = None       # set t1 instance to empty
#       t1.size = 0
#     if not t2.is_empty():   # attach t2 as right subtree of node
#       t2._root._parent = node
#       node._right = t2._root
#       t2._root = None       # set t2 instance to empty
#       t2._size = 0

# ############

# P = LinkedBinaryTree()
# P._add_root('Providence')
# P._add_left(P.root(), 'Chicago')
# P._add_right(P.root(), 'Seattle')
# P._add_left(P.left(P.root()), 'Baltimore')
# P._add_right(P.left(P.root()), 'New York')
# P._add_left(P.right(P.root()), 'Busan')
# P._add_right(P.right(P.root()), 'Seoul')
# P._add_left(P.left(P.left(P.root())), 'Baltimore')
# P._add_right(P.left(P.left(P.root())), 'New York')
# print(P)
# print ('\n------------------------------------\n')

# Q = LinkedBinaryTree()
# Q._add_root('-')
# Q._add_left(Q.root(),'/')
# Q._add_right(Q.root(),'+')
# Q._add_left(Q.left(Q.root()), 'X')
# Q._add_right(Q.left(Q.root()), '+')

# Q._add_left(Q.right(Q.root()), 'X')
# Q._add_right(Q.right(Q.root()),6)

# Q._add_left(Q.left(Q.left(Q.root())), '+')
# Q._add_right(Q.left(Q.left(Q.root())), '3')
# Q._add_left(Q.left(Q.left(Q.left(Q.root()))), '3')
# Q._add_right(Q.left(Q.left(Q.left(Q.root()))), '1')

# Q._add_left(Q.right(Q.left(Q.root())), '-')
# Q._add_right(Q.right(Q.left(Q.root())), '2')
# Q._add_left(Q.left(Q.right(Q.left(Q.root()))), '9')
# Q._add_right(Q.left(Q.right(Q.left(Q.root()))), '5')

# Q._add_left(Q.left(Q.right(Q.root())), '3')
# Q._add_right(Q.left(Q.right(Q.root())), '-')

# Q._add_left(Q.right(Q.left(Q.right(Q.root()))), '7')
# Q._add_right(Q.right(Q.left(Q.right(Q.root()))), '4')

# print(Q)

import time
import random
from collections import deque

class Node:
    def __init__(self, value=None, levels=None):
        self.value = value
        self.forward = levels if levels is not None else []

class SkipList:
    def __init__(self, max_level, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = Node(levels=[None]*max_level)
        self.level = 0

    def random_level(self):
        lvl = 1
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * self.max_level
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current is None or current.value != value:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level, lvl):
                    update[i] = self.header
                self.level = lvl
            new_node = Node(value, [None]*lvl)
            for i in range(lvl):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

    def remove(self, value):
        update = [None] * self.max_level
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and self.header.forward[self.level - 1] is None:
                self.level -= 1
            return True
        return False

    def update(self, old_value, new_value):
        if self.remove(old_value):
            self.insert(new_value)
            return True
        return False

# Define timing function
def time_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return end - start, result
    return wrapper

# Benchmarking function
def perform_operations(data_structure, data, operation):
    times = []
    for value in data:
        time_elapsed, _ = time_function(lambda: operation(data_structure, value))()
        times.append(time_elapsed)
    return sum(times) / len(times)

# Data and structure setup
data_size = 10000
data = random.sample(range(data_size * 10), data_size)

# Initialize data structures
skip_list = SkipList(10, 0.5)
array_list = []  # Using list to simulate an array
linked_list = deque()

# Insert data into structures
for number in data:
    skip_list.insert(number)
    array_list.append(number)
    linked_list.append(number)
array_list.sort()  # Simulate sorted array insertion cost

# Measure and print times for search operations
print("Skip List Search Time: {:.6f}s".format(perform_operations(skip_list, data, lambda s, x: s.search(x))))
print("Array List Search Time: {:.6f}s".format(perform_operations(array_list, data, lambda s, x: x in s)))
print("Linked List Search Time: {:.6f}s".format(perform_operations(linked_list, data, lambda s, x: x in s)))
