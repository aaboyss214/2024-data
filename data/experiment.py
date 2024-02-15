import random
import time
arr = [1,2,3,4,5,6,7,8,9,10]

while True:
    random.shuffle(arr)
    time.sleep(1)
    print(arr)