def min(arr):
    minn = 0
    for i in range(1, len(arr)):
        if arr[minn] > arr[i]:
            minn = i
    return minn





before = [180, 15, 123, 569, 85, 10]
after=[]

print("정렬 전 :", before)
for _ in range(len(before)):
    minindex = min(before)
    after.append(before[minindex])
    del (before[minindex])
print('정렬 후 :', after)

# def findMinIdx(ary):
#     minIdx = 0
#     for i in range(1, len(ary)):
#         if ary[minIdx] > ary[i]:
#             minIdx = i
#     return minIdx
#
#
#
# before = [188, 162, 168, 120, 50, 150, 177, 105, 10, 22, 5]
# after = []
#
#
# print('정렬 전 -->', before)
# for _ in range(len(before)):
#     minPos = findMinIdx(before)
#     after.append(before[minPos])
#     del (before[minPos])
# print('정렬 후 -->', after)
