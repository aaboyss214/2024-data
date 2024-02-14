sum = 0;
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

# def fibo(n) :
# 	if n == 0 :
# 		return 0
# 	elif n == 1 :
# 		return 1
# 	else :
# 		return fibo(n-1) + fibo(n-2)
# print()
# number = int(input())
# print('피보나치 수 --> 0 1 ', end='')
# for i in range(2, number):
# 	print(fibo(i), end=' ')
