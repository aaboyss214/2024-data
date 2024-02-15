class Node():
    def __init__ (self):
        self.data = None
        self.plink = None
        self.nlink = None

def link_node(i):
    global head, current, Arr
    node = Node()
    node.data=Arr[i]
    if head is None:
        head = node
        current = node
    else:
        current.plink = node
        node.nlink = current
        current = node


head, current, pre = None, None, None
Arr=['다현','정연','쯔위','사나','지효']

def print_plink():
    global head, current
    current = head
    print('정방향 --->  ',current.data, end=' ')
    while current.plink is not None:
        current=current.plink
        print(current.data, end=' ')
    print()


def print_nlink():
    global current
    print('역방향 --->  ', current.data, end=' ')
    while current.nlink is not None:
        current = current.nlink
        print(current.data, end=' ')


if __name__=="__main__":
    for i in range(5):
        link_node(i)
    print_plink()
    print_nlink()
