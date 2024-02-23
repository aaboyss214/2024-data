T = int(input())
def divider(number_):
    arr=[2,3,5,7,11]
    arr2 = []
    for i in arr:
        count = 0
        while True:
            if number_ % i == 0:
                number_ = number_ / i
                count = count + 1
            else:
                arr2.append(count)
                break
    return arr2

for test_case in range(1, T + 1):
    number = int(input())
    print(f'#{test_case}', end=' ')
    number2 = divider(number)
    for i in range(5):
        print(number2[i],end=' ')
    print()