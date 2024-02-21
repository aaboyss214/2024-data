T = int(input())
for test_case in range(1,T+1):
    n, m = map(int,input().split())
    max = 0
    #대소는 정해져있지 않다.

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if n >= m:
        big_arr = arr1
        small_arr = arr2
        big = n
        small = m
    else:
        big_arr = arr2
        small_arr = arr1
        big = m
        small = n

    for j in range(big - small +1):
        sum = 0
        for i in range(small):
            sum = sum + small_arr[i]*big_arr[j+i]
        if sum >= max:
            max = sum
    print(f'#{test_case} {max}')