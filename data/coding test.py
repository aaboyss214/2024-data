def day_count(mounth):
    total = 0
    day_count_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in day_count_arr[0:mounth-1]:
        total = total + i
    return total

if __name__=="__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        m1, d1, m2, d2 = map(int, input().split())
        print(f'#{test_case} {day_count(m2) + d2 - (day_count(m1) + d1)+1}')
