<<<<<<< HEAD
test_case = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse = -1)
sum = 0
for i in range(test_case):
    sum += arr1[i]*arr2[i]
print(sum)
=======
s = input('이진수를 입력하세요: ')
_10 = 0
for i in range(len(s)):
    if s[i:i+1] == '1':
       _10 += pow(2,len(s)-1-i)
print(_10)
>>>>>>> 4fdb824800988f7f0f4da369d00b5fadffbbd0bd
