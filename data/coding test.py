
for test_case in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(2, T-2):
        a, b, c, d = arr[i-2], arr[i-1], arr[i+1], arr[i+2]
        if arr[i] > a and arr[i] > b and arr[i] > c and arr[i] > d:
            if a >= b:
                max1 = a
            else:
                max1 = b 

            if c >= d:
                max2 = c
            else:
                max2 = d

            if max1 > max2:
                max = max1
            else:
                max = max2
            
            count = count + arr[i] - max
    print(f'#{test_case} {count}')