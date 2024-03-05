T = int(input())

for test_case in range(1, T+1):
    arr = []
    count = 2
    number = input()
    number2 = number
    while len(arr) != 10:
        for i in range(len(number2)):
            if int(number2[i]) not in set(arr):
                arr.append(int(number2[i]))
        number2 = str(int(number) * count)
        count = count + 1
    print(f'#{test_case} {(count-2)*int(number)}')
