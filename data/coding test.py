# # '''
# # 4      << 자료구조 개수
# # 0 1 1 0 << 큐or스택 결정 큐 = 0 스택 = 1
# # 1 2 3 4 << 큐 스택 스택 큐
# # 3 << 삽입할 수열의 길이
# # 2 4 7 << 삽입할 수열
# # 출력은 pop되는 걸 받는 듯
# # 스택 = 후입선출
# # 큐 = 선입선출
# # 팝된걸 다음에 넣고 또 팝된걸 다음에 넣고 마지막으로 pop된걸 출력하는 시스템
# # 이해했다..드디어..


# # 자리수 만큼의 리스트를 만드는건 런타임 에러 나올려나
# # 어떡하지.. 그냥 조건문 사용해서 리스트 하나로 해야할듯

# # '''

# m = int(input())
# arr1 = list(map(int,input().split()))

# arr2 = list(map(int,input().split()))
# n = int(input())
# arr3 = list(map(int,input().split()))

# arr2=[arr2[i] for i in range(len(arr2)) if arr1[i] == 0]

# for element in arr3:
#     for i in range(len(arr2)):
#             element, arr2[i] = arr2[i], element
#     print(element, end=' ')

from collections import deque

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m = int(input())
arr3 = list(map(int, input().split()))

result = deque(arr3)
for i in range(n):
    if arr1[i] == 0:#큐
        result.appendleft(arr2[i])
print(result)
for i in range(m):
    print(result.popleft(), end=' ')