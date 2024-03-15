print('==========================')
list1 = list(map(int, input().split()))
avg = sum(list1)/3
var = 0
for i in list1:
    var = var + pow(i-avg,2)
var = var / 3
std = var**(1/2)
print('==========================')
print('===파이썬 중간고사 결과===')
print('==========================')
print('전체 수강생 수 : ', 3)
print('평균 : ', avg)
print('분산 : ', var)
print('표준편차 : ', std)
