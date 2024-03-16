n = int(input())
for i in range(n*2-1):
    if i < n:
        print(' '*(n-1-i)+'*'*(2*i+1))
    else:
        print(' '*(i-n+1)+'*'*(2*(2*(n-1)-i)+1))

# n = int(input())

# temp = n-1
# stars = 1
# for i in range(n-1):
#     print(' '*temp+'*'*stars)
#     temp -= 1
#     stars += 2

# for i in range(n):
#     print(' '*temp+'*'*stars)
#     temp += 1
#     stars -= 2

# a, b = map(int,input().split())
# #5 3
# p = 0
# count = 0
# x,y = 0,0#x = 좌우, y = 상하

# for i in range(a*b):
#     if p%4 == 0:#오른쪽
#         x += 1
#         if x==b:
#             count += 1
#             p=1
#             x=0
#     elif p%4 == 1:#아래
#         y += 1
#         if y==a:
#             count += 1
#             p=2
#             x=0
            
#     elif p%4 == 2:#왼쪽
        
#     elif p%4 == 3:#위로
#         pass