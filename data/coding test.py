repetition= int(input())
a=[]
count = 1
for _ in range(repetition):
    number = int(input())
    a.append(number)

for i in a:
    sum = 0
    for j in range(i):
        if (j+1)%2==1:
            sum = sum +j+1
        else:
            sum = sum -(j+1)
    print(f'#{count} {sum}')
    count = count +1