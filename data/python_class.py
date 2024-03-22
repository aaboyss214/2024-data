s = input('이진수를 입력하세요: ')
_10 = 0
for i in range(len(s)):
    if s[i:i+1] == '1':
       _10 += pow(2,len(s)-1-i)
print(_10)
