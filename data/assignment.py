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
def Data_assign(name_email):
    global head, current, pre
    node = Node()
    node.data = name_email

    if head is None:
        head = node
        return
    if head.data[1] > name_email[1]:
        node.link = head
        head = node
        return
    current = head
    while current.link is not None:
        pre = head
        current = current.link
        if current.data[1] > name_email[1]:
            pre.link = node
            node.link = current
            return
    current.link = node
def Print_Data(start):
    current = start
    if start is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()

head, current, pre = None, None, None

if __name__ == "__main__":
    while True:
        name = input('이름--> ')
        if name == '':
            break
        email = input('이메일--> ')
        Data_assign([name,email])
        Print_Data(head)



