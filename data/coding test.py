# 대칭차집합은 전체 집합에서 교집합 뺀것
# 대칭차집합 원소 개수 출력

a, b = map(int, input().split())
arr_a = set(map(int, input().split()))
arr_b = set(map(int, input().split()))
print((arr_a|arr_b)-(arr_a&arr_b))
