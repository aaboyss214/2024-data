number = int(input())
arr = [[] for _ in range(number)]

for i in range(number):
    for j in range(number*i+1,(number*(i+1))+1):
        arr[i].append(j)

for i in range(number):
    if i % 2 ==0:
        pass
    else:
        arr[i].reverse()
    for j in range(number):
        print(' '*(3-len(str(arr[i][j]))),arr[i][j],end='')
    print()