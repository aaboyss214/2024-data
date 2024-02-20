T=int(input())
for test_case in range(1, T+1):
    hour1, minute1, hour2, minute2 = map(int, input().split())
    hour, minute = 0, 0
    if minute1 + minute2 >= 60:
        minute = minute1 + + minute2 - 60
        hour = hour + 1
    else:
        minute = minute1 + + minute2
    if hour1 + hour2 > 12:
        hour = hour1 + hour2 - 12
    else:
        hour = hour1 + hour2

    if minute1 + minute2 >= 60:
        minute = minute1 + + minute2 - 60
        hour = hour + 1
    else:
        minute = minute1 + + minute2
    print(f'#{test_case} {hour} {minute}')