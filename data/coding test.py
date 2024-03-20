#11111111111111111111111111111111
input()
list1 = input().split()
input()
list2 = input().split()
print(' '.join([ str(list1.count(a)) for a in list2 ]))


#22222222222222222222222222222222
# from collections import Counter

# input()
# list1 = input().split()
# input()
# list2 = input().split()
# counter = Counter(list1)
# print(' '.join(str(counter[a]) for a in list2))

#33333333333333333333333333333333
# input()
# list1 = input().split()
# input()
# list2 = input().split()
# counts = {}
# for item in list1:
#     counts[item] = counts.get(item, 0) + 1
# print(' '.join(str(counts.get(item, 0)) for item in list2))
