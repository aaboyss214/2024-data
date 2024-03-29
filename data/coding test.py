# count, word_len = map(int,input().split())
# dic1 = {}
# for _ in range(count):
#     word = input()
#     if len(word) >= word_len:
#         if word in dic1:
#             dic1[word] += 1
#         else:
#             dic1[word] = 1




def custom_sort(word_list, m):
    # 단어의 길이가 m 이상인 단어만 선택
    filtered_words = [word for word in word_list if len(word) >= m]

    # 각 단어의 빈도수를 저장하는 딕셔너리 생성
    word_freq = {}
    for word in filtered_words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # 우선순위에 따라 정렬
    sorted_words = sorted(word_freq, key=lambda x : (-word_freq.get(x, 0), -len(x), x))

    return sorted_words

# 입력 받기
n , m = map(int, input().split())
words = [input() for _ in range(n)]

# 결과 출력
for i in custom_sort(words, m):
    print(i)