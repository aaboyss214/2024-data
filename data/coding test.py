n , m = map(int, input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
max = 1
for i in range(n):
    for j in range(m):
        size = 1
        length = 0
        while True:
            if i + size >= n or j + size >= m:
                break 
            if arr[i][j] == arr[i][j+size] == arr[i+size][j] == arr[i+size][j+size]:
                length = size + 1
            if length > max:
                max = length
            size += 1

print(max)