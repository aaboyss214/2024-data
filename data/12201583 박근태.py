
class Empty(Exception):
  ''' Error attempting to access an element from an empty container.'''
  pass

class _DoublyLinkedBase:
  '''A base class providing a doubly linked list representation.'''

  #-----------------------------------------------------------------
  class _Node:
    '''Lightweight, nonpublic class for storing a doubly linked node.'''
    __slots__ = '_element', '_prev', '_next'        # streamline memory

    def __init__(self, element, prev, next): # initialize node's field
      self._element = element       # element to be stored
      self._prev = prev             # Previous node reference
      self._next = next             # next node reference
  #-------------------------------------------------------------------
  def __init__(self):#header와 trailer 미리 생성
    '''Create an empty list.'''
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer      # trailer is after header
    self._trailer._prev = self._header      # header is before trailer
    self._size = 0                          # Number of elements

  def __len__(self):
    '''Return the number of elements in the list.'''
    return self._size

  def is_empty(self):
    '''Return True if list is empty.'''
    return self._size == 0

  def _insert_between(self, e, predecessor, successor):
    '''Add element e between two existing nodes and return new node.'''
    newest = self._Node(e, predecessor, successor) # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    '''Delete nonsentinel node from the list and return its element.'''
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1                 # record deleted element
    element = node._element
    node._prev = node._next = node._element = None # deprecate node
    return element      # return deleted element

class PositionalList(_DoublyLinkedBase):
  '''A sequential container of elements allowing positional access'''

  # -------------- nested Position Class ----------------------------
  class Position:
    '''An abstraction representing the location of a single element'''

    def __init__(self, container, node):
      '''Constructor should not be invoked by user'''
      self._container = container
      self._node = node
      
      
    def element(self):
      '''Return the element stored at this Position'''
      return self._node._element

    def __eq__(self, other):
      '''Return True if other is a Position representing the same location'''
      return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
      '''Return True if other does not represent the same location'''
      return not (self == other)

    #-------------------- Utility Methods ---------------------------

  def _validate(self, p):
    '''Return position's node or raise appropriate error if invalid'''
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._next is None:   # convention for depricated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    ''' Return Position instance for a given node(or None if sentinel)'''
    if node is self._header or node is self._trailer:
      return None             #boundary violation
    else:
      return self.Position(self, node)    # legitimate position

  # ------------------- Accessors ----------------------------
  
    
  def find_position(self, e):
    '''Return the first Position containing element e, or None if not found.'''
    cursor = self.first()
    while cursor is not None:
      if cursor.element() == e:
        return cursor
      cursor = self.after(cursor)
    return None
  
  def first(self):
    ''' Return the first Position in the list (or None if list is empty)'''
    return self._make_position(self._header._next)

  def last(self):
    '''Return the last Position in the list (or None if list is empty)'''
    return self._make_position(self._trailer._prev)

  def before(self, p):
    '''Return the Position just before Position p (or None if p is first)'''
    node = self._validate(p)
    return self._make_position(node._prev)

  def after(self, p):
    '''Return the Position just after Position p (or None if p is last)'''
    node = self._validate(p)
    return self._make_position(node._next)

  def __iter__(self):
    '''Generate a forward iteration of the elements of the list'''
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)


  #-------------- Mutators ------------------------------
  # override inherited version to return Position, rather than Node
  def _insert_between(self, e, predecessor, successor):
    '''Add element between existing nodes and return new Position'''
    node = super()._insert_between(e, predecessor, successor)
    return self._make_position(node)

  def add_first(self, e):
    '''Insert element e at the front of the list and return new Position'''
    return self._insert_between(e, self._header, self._header._next)

  def add_last(self, e):
    '''Insert element e at the back of the list and return new Position'''
    return self._insert_between(e, self._trailer._prev, self._trailer)

  def add_before(self, p, e):
    '''Insert element e into list before Position p and return new Position'''
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)

  def add_after(self, p, e):
    '''Insert element e into list after Position p and return new Position.'''
    original = self._validate(p)
    return self._insert_between(e, original, original._next)

  def delete(self, p):
    '''Remove and return the element at Position p'''
    original = self._validate(p)
    return self._delete_node(original) # inherited method returns element

  def replace(self, p, e):
    '''
    Replace the element at Position p with e.
    Return the element formerly at Position p.
    '''
    original = self._validate(p)
    old_value = original._element
    original._element = e
    return old_value

'''
If you enter an alphabet, insert the alphabet in the string as left, 
and if not, insert it at the end of the list. 
If more alphabets are entered than necessary, insert them to the right of the already existing alphabet.
'''

class NameBasedPositionalList(PositionalList):
  def __init__(self, name):
    super().__init__()#Using the super() function to use the member variables of the parent class
    self._name = list(name.lower())#내이름저장

  def add_character(self, alpha):#A node with a value is created, and the position of the node is the data of the object L.
    if alpha.lower() in self._name:
        current_position = self.first()
        last_position = False
        #Locate the last location where alpha is located.
        #Assign the last location of alpha to the last_position variable
        #Check all elements of the list through the while statement. When the last position is assigned to the current position, the while statement ends.
        while  current_position:
            if  current_position.element() == alpha.lower():
                last_position =  current_position
            current_position = self.after(current_position)

        #Run if statement if alpha is on the list
        if last_position:
            # 마지막 위치의 바로 다음에 삽입
            self.add_after(last_position, alpha.lower())                                  #여기서 노드를 만든다.
        else:
            # 해당 문자가 리스트에 없으면 처음에 삽입
            self.add_first(alpha.lower())                                                 #여기서 노드를 만든다. 처음에 값을 삽입하면 이 코드를 통해 값이 self에 삽입된다.
    ############################################################여기 사이 코드만 이해하면 된다. 이제
    else:
        # 이름에 없는 문자는 리스트 끝에 추가
        self.add_last(alpha.lower())                                                      #여기서 노드를 만든다.

  def __str__(self):
    arr = ''
    cursor = self.first()
    while cursor is not None:
      arr += str(cursor.element()) + ', '
      cursor = self.after(cursor)
    return '<' + arr + '>'
  
  # def __str__(self):
  #   return '<' + ', '.join(str(x) for x in self) + '>'                      #아래의 명령문을 예로 들면 L이라는 객체는 포지션이라는 객체가 여러개 연결되어 있는 것을 나타낸다.
                                                                              #애초에 노드는 부모 클래스에서 완전히 만들어진 상태 positional 클래스에서는 포지션만 신경쓴다. 포지션은 서로간의 직접적인 연결이되어있지 않다. 그저 연결되어 있는 노드들을 메서드로 순회해가며 포지션을 리턴하는 것
  # for x in self의 self는 __iter__메소드 덕분에 in 뒤에 쓸 수 있는 것이다.

# test code
if __name__=='__main__':
    L = NameBasedPositionalList('ParkGeunTae')#L은 포지션이 담겨져있는 포지션 리스트
    L.add_character('P')                                                      #들어온 값을 가지는 노드는 어디서 만들어지는 거야
    L.add_character('D')
    L.add_character('F')
    L.add_character('G')
    L.add_character('E')
    L.add_character('N')
    L.add_character('N')
    L.add_character('A')
    L.add_character('A')
    L.add_character('T')
    L.add_character('X')
    print(L.first())                                                        #포지션을 출력하면 주소만 나온다
    print(L.before(L.last()))                                               #이것도 포지션을 출력하는 것이니 주소만 나온다.
    print('Positional List based on the name: ', L)


#position클래스는 인수로 받는 노드를 가르키는 객체
#각 메서드는 특정 값이 아니라 position 클래스의 객체를 리턴하는 것 
#포지션 객체의 속성은 특정 노드다.
