T=int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = [input().split() for _ in range(n)]
    row = '0'.join([''.join(i) for i in arr])
    column = '0'.join(''.join(i) for i in list(zip(*arr)))
    row_sum = sum([True for i in row.split('0') if i == '1'*k])
    column_sum = sum([True for i in column.split('0') if i == '1'*k])
    print(f'#{test_case} {row_sum + column_sum}')