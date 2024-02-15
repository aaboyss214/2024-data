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
