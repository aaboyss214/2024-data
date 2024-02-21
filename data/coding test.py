T = int(input())
for test_case in range(1,T+1):
    money = int(input())
    answer=[0]*8
    charge=[50000,10000,5000,1000,500,100,50,10]
    for i in range(8):
    if money//charge[i] > 0:
    answer[i] = money//charge[i]
    money = money%charge[i]
    print(f'#{test_case}')
    print(*answer)