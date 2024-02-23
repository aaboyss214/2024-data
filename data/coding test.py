T = int(input())
for test_case in range(1, T + 1):
    number_alp = int(input())
    arr = []
    count = 0
    for _ in range(number_alp):
        alp , n = map(str, input().split())
        arr.append(alp)
        arr.append(int(n))
    print(f'#{test_case}')
    for i in range(number_alp):

        for _ in range(arr[2*i +1]):
            print(arr[2*i],end='')
            count = count +1
            if count % 10 == 0:
                print()
    print()