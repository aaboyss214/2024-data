import random
import math
class Node():
    def __init__ (self):
        self.data = None
        self.link = None

Arr=[]
head=None
current=None
pre=None
def sort_node(i):
    global Arr, head, current, pre

    node = Node()
    node.data=Arr[i]

    if head is None:
        head = node
        return

    current = head
    # 제일 앞에 올때
    if node.data[3] < current.data[3]:
        node.link = head
        head = node
        return
    # 중간에 올때


    while current.link is not None:
        pre = current
        current = current.link
        if current.data[3]>=node.data[3]:
            pre.link = node
            node.link = current
            return
        else:
            pass


    # 제일 끝에 올때
    current.link = node
    node.link = head

def print_node() :
    global head
    current = head
    while True:
        if current == None:
            pass
        else:
            while current.link != head:
                print(current.data[0], '편의점, 거리:', current.data[3])
                current = current.link

            print()


if __name__=="__main__":
    for i in range(10):
        x=random.randint(1,100)
        y=random.randint(1,100)
        location = chr(ord('A')+i)
        Arr.append((location, x , y, math.sqrt(pow(x,2)+pow(y,2))))
        sort_node(i)
        print_node()

