sum = 0
pre1 = 0
pre2 = 1
number = int(input())
print(pre2, end = ' ')
while number >= 2:
	sum = pre1 + pre2
	number = number - 1
	print(sum, end=' ')
	pre1=pre2
	pre2=sum

def fibo(n) :
	if n == 0 :
		return 0
	elif n == 1 :
		return 1
	else :
		return fibo(n-1) + fibo(n-2)
# print()
# number = int(input())
# print('피보나치 수 --> 0 1 ', end='')
# for i in range(2, number):
# 	print(fibo(i), end=' ')
print()
number = int(input())
memo = [None for _ in range(number)]#컴프리헨션

def fibo_memo(n: int, memo: list) -> int:
	if memo[n] is not None:
		return memo[n] #한번 계산한 값을 사용하는 것
	if n<2:
		result = n
	else:
		result = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
		memo[n]=result
	return result


for i in range(0,number):
	print(i,end = ' ')
	print(fibo_memo(i,memo))








