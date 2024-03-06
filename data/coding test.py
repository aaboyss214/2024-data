t = int(input())
for test_case in range(1, t+1):
    str_ = input()
    result = True
    if str_ != str_[::-1]:
        result = False
        print(2)
    elif str_[:len(str_)//2] != str_[:len(str_)//2:-1]:
        result = False
        print(3)
    elif str_[len(str_)//2+1:] != str_[-1:-(len(str_)//2+1):-1]:
        result = False
        print(4)
    if result:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
