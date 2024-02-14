class Node():
    def __init__ (self):
        self.data = None
        self.link = None
'''
1. 이름, 이메일 입력받기
2. 노드 하나 만들고 이름, 이메일을 데이터에 저장
3. head or current가 None 이면 그냥 노드 데이터 저장
4. None아니면 즉 node가 있을 시 있는 node와 이메일 비교
5. 1개가 있으면 한개와만 비교하고 링크랑 head를 정렬에 맞게 조정, 일단 current를 제일 뒷노드로 설정
6. 2개 이상 있으면 뒤에서부터 비교 

노드 만들고 그 노드의 데이터에 값 할당하는 함수 하나
만들어진 노드들의 이메일을 비교하는 함수 하나
노드 데이터들을 출력하는 함수 하나
전역 변수로는 head, current, pre 만들면 될듯
'''
def Data_assign():
    global head, current, pre, count
    while True:
        node = Node()
        print()
        name = input('이름--> ')
        if name == '':
            return
        email = input('이메일--> ')
        node.data = [name, email]
        if head is None:
            head = node
            current = node
        else:
            if current.link is None:
                if head.data[1]>node.data[1]:
                    node.link = head
                    head = node
                    current = node
                else:
                    head.link = node
                pre = head
            else:
                while True:
                    if current.data[1] < email:
                        pre = current
                        current = current.link
                    elif current.link is None:
                        current.link = node
                        break
                    elif head.data[1] > email:
                        node.link = head
                        head = node
                        break
                    elif current.data[1] > email:
                        node.link = current
                        pre.link = node
                        break
                    else:
                        node.link = current.link
                        current.link = node
        count = count+1
        current = head
        pre = head
        Print_Data(head)
def Print_Data(start):
    global count
    for _ in range(count):
        print(start.data, end=' ')
        start=start.link

head, current, pre = None, None, None
count = 0

if __name__ == "__main__":
   Data_assign()




