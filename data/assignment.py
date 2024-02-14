import random

class Node():
    def __init__ (self):
        self.data = None
        self.link = None

head, current, pre = None, None, None

def generate_node():
    global head, current, pre
    for _ in range(6):
        node = Node()
        a = random.randint(1,45)
        node.data = a
        if head is None:
            head = node
            current = node
        else:

            while current.link is not None:
                current = current.link
            current.link=node
        print_node(current)


def print_node(start):
    print(start.data, end=' ')


if __name__=="__main__":
    generate_node()
