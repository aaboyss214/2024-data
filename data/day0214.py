from collections import deque

# input_data = list(map(int, input().split()))
# print(input_data)
# n=input_data[0]
# m=input_data[1]
# k=input_data[2]
# x=input_data[3]
# print(n, m, k, x)

n, m, k, x = map(int, input().split())
# print(n, m, k, x)
g=[[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    g[start].append(end)

d = [-1]*(n+1)
d[x] = 0

q=deque([x])
while q:
    now = q.popleft()
    for next in g[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if d[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
