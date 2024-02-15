import random
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		return
	top += 1
	stack[top] = data

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	return stack[top]
SIZE = 10
stack = [ None for _ in range(SIZE)]
top = -1

if __name__=="__main__":
	arr=["빨강", "파랑", "초록", "노랑", "보라", "주황"]
	random.shuffle(arr)
	print('과자집에 가는길 : ')
	for stone in arr:
		push(stone)
		print(stone, '-->', end='')
	print('과자집')

	print('우리집에 가는길 : ')
	while top != -1:
		print(pop(), '-->', end='')
	print('우리집')


