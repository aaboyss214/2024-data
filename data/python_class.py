# import random

# def num_mafla():
#     dict1 = {6:[2,2,1,1],7:[3,2,1,1],8:[3,3,1,1],9:[4,3,1,1],10:[4,4,1,1]}
#     dict2 = {0:'당신의 직업은 마피아입니다.',1:'당신의 직업은 시민입니다.',2:'당신의 직업은 경찰입니다.',3:'당신의 직업은 의사입니다.'}
#     while True:
#         number = int(input('인원 수를 입력해주세요 : '))
#         if number <= 10 and number >= 6:
#             break
#         else:
#             print('마피아 게임의 적정 인원은 6~10명 입니다.')
#     countlist = dict1[number]            
#     count = 0
#     for i in range(number):
#         with open('{}.txt'.format(i+1),'w',encoding = 'utf-8') as file:
#             while True:
#                 randnumber = random.randrange(0,4)
#                 if countlist[randnumber] > 0:
#                     file.write(dict2[randnumber])
#                     countlist[randnumber] = countlist[randnumber] - 1
#                     break

        
# num_mafla() 



import random

def lotto():
    arr = []
    while len(arr) < 6:
        number = random.randrange(1,46)
        if number not in arr:
            arr.append(number)
    return arr 

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def Prob_win(n):
    return 100/(factorial(45)/(factorial(45-n)*factorial(n)))

num = lotto()

print('로또 1등 당첨번호는 {},{},{},{},{},{}입니다.'.format(*num))
print('로또 1등 당첨확률은 {:.7f}% 입니다.'.format(Prob_win(len(num))))


# def N_gram(n,text):
#     for i in range(len(text)-n+1):
#         print(text[i:i+n])
        

# text = input('원하는 text를 입력하세요: ')
# n = int(input('원하는 N-gram 수를 입력하세요: '))

# N_gram(n, text)


