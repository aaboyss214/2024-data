
repetition= int(input())
a=[]

for i in range(repetition):
    a.append(list(map(int, input().split())))
    max_num=max(a[i])
    min_num=min(a[i])
    a[i].remove(max_num)
    a[i].remove(min_num)

for j in range(repetition):
    sum = 0
    for k in a[j]:
        sum = sum + k
    print(f'#{j+1} {round(sum/len(a[j]))}')
