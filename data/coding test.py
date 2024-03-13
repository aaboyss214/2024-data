# T = int(input())
# for test_case in range(1, T+1):
#     number, count = map(int, input().split())
#     arr = list(i for i in str(number))
#     max = max(arr)
#     if arr.count(max) > 1:
#         pass
#     else:
#         index = arr.index(max)
#         if count > 1:

#         else:
#             arr[0], arr[index] = arr[index], arr[0]
#     print(arr)

# max값 새 배열에 pop 하고 나머지는 그냥 배열에 붙이면 되잖아
# 1. max값이 중복되어있으면 제일 뒤에있는 수를  pop해야하는데
# 2. arr.pop(원하는위치) >> reverse.arr 해서 index 찾아서 하면 될듯
# 이렇게 하는게 아니다 요소를 교환해야해서 a, b = b, a 써야하나...... 흠..

def dfs(cnt):
    global ans
    if cnt == n:
        ans = max(ans, int("".join(map(str, lst))))
        return
 
    for i in range(Length - 1):
        for j in range(i + 1, Length):
            lst[i], lst[j] = lst[j], lst[i]
            chk = int("".join(map(str, lst)))
            if (cnt, chk) not in visited:
                dfs(cnt + 1)
                visited.append((cnt, chk))
            lst[i], lst[j] = lst[j], lst[i]

if __name__=="__main__": 
    T = int(input())
    
    for i in range(1, T + 1):
        num, n = input().split()
        n = int(n)
        lst = list(map(int, num))
        Length = len(lst)
        visited = []
        ans = 0
        dfs(0)
        print(f'#{i} {ans}')