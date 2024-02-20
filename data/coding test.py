T = int(input())
for test_case in range(1, T+1):
    result1=1
    result2=1
    result3=1
    arr=[]
    arr = [input().split() for _ in range(9)]
    #3x3
    for p in range(0,9,3):
        for j in range(0,9,3):
            list1=[]
            for i in range(3):
                for k in range(3):
                    list1.append(arr[j+i][k+p])
                list1.sort()
            if ''.join(list1) == '123456789':
                pass
            else:
                result3 = 0


    #세로
    new_arr = [''.join(i) for i in list(zip(*arr))]
    for i in range(1,10):
        if len(set(new_arr[i-1])) == 9:
            pass
        else:
            result2=0

    for i in range(9):
        arr[i].sort()

    #가로
    new_arr = ''.join([''.join(i) for i in arr])
    if new_arr == '123456789'*9:
        pass
    else:
        result1=0

    #결과출력
    if result1 == 1 and result2 == 1 and result3 ==1:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')
