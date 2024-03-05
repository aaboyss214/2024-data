T = int(input())
for test_case in range(1, T+1):
    test_case_ = int(input())
    arr = list(map(int,input().split()))
    set_ = set(arr)
    max = 0
    max_count = 0
    for i in set_:
        if arr.count(i) > max_count:
            max_count = arr.count(i)
            max = i
        elif arr.count(i) == max_count:
            if i > max:
                max = i
    print(f'#{test_case} {max}')
