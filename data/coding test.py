T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    arr = list(map(int,input().split()))
    min = abs(arr[0])
    count = 0
    for i in range(len(arr)):
        if min > abs(arr[i]):
            min = abs(arr[i])
        elif min == abs(arr[i]):
            count = count + 1
        else:
            pass
    print(f'#{test_case} {min} {count}')
