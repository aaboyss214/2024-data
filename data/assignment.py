class Node():
    def __init__ (self):
        self.data = None
        self.link = None
def print_node(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()
def list(name_email):
    global pre, head, current
    node = Node()
    node.data = name_email
    if head is None:
        head = node
        return
    if head.data[1]>name_email[1]:
        node.link = head
        head = node
        return
    current = head
    while current.link is not None:
        pre =  current
        current = current.link
        if current.data[1]>name_email[1]:
            pre.link = node
            node.link = current
            return
    current.link = node

pre = None
head = None
current = None

if __name__ == "__main__":

    while True:
        name = input("이름--> ")
        if name == '':
            break
        email = input("이메일--> ")
        list([name,email])
        print_node(head)
