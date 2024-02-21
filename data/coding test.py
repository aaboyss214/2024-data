T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]

    arr1 = arr#270
    for i in range(n):
        arr1[i].reverse()
    arr1 = list(zip(*arr1))

    arr2 = arr#90
    arr2.reverse()
    arr2 = list(zip(*arr2))

    arr3 = arr#180

    print(f'#{test_case}')
    for j in range(n):
        print(''.join(arr2[n-1-j]), end=' ')
        print(''.join(arr3[j]), end=' ')
        print(''.join(arr1[j]))