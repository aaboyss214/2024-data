# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# #1 2 3 4 5 6 7 8 9
# for tc in range(1, int(input()) + 1):
#     N = int(input())#N=3
#
#     snail = [[0] * N for _ in range(N)]#2차원 배열 만들기 [[0,0,0],[0,0,0],[0,0,0]]
#     r, c, d = 0, 0, 0
#
#     for num in range(1, N ** 2 + 1):#배열에 수 오름차순으로 삽입 num은 1에서 9
#         snail[r][c] = num#배열에 원소 넣기. 시작은 1로
#
#         nr, nc = r + dr[d], c + dc[d]#1 : nr = 0 nc = 1
#
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
#             d = (d + 1) % 4
#             nr, nc = r + dr[d], c + dc[d]
#
#         r, c = nr, nc
#
#     print(f'#{tc}')
#     for line in snail:
#         print(*line)


            # 3 2 2 1 1
            # 4 3 3 2 2 1 1
            # 5 4 4 3 3 2 2 1 1
            # 6 5 5 4 4 3 3 2 2 1 1
#배열에 값을 넣는 방식으로

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    j , q1, q2 = 0 , N-1 , 0
    p , k = 0 , -1
    for i in range(N**2):
        if p % 4 == 0: #오른쪽으로
            k = k + 1
            arr[j][k] = i+1


            if k == q1:
                p = 1


        elif p % 4 == 1:
            j = j + 1
            arr[j][k] = i+1 #아래쪽으로


            if j == q1:
                p = 2


        elif p % 4 == 2:
            k = k - 1
            arr[j][k] = i+1 #왼쪽으로


            if k == q2:#0
                p = 3
                q2 = q2 +1

        elif p % 4 == 3:
            j = j - 1
            arr[j][k] = i+1 #위쪽으로


            if j == q2:#1
                p = 0
                q1 = q1 - 1


    print(f'#{test_case}')
    for answer in arr:
        print(*answer)
