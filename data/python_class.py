import time
n = 100000
start = time.time()
squares = [k*k for k in range(1, n+1)]
end = time.time()
print(f'{start-end}')

start = time.time()
squares = []
for k in range(1, n+1):
    squares.append(k*k)
end = time.time()
print(f'{start-end}')

