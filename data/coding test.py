T = int(input())
for test_case in range(1,T+1):
    len_ = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{test_case}', end=' ')
    print(*numbers)