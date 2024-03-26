num = int(input('정수를 입력하세요 : '))

if num != 0:
    if num > 0:

        a = 1
    elif num <= 0:

        a = num
        
    divisor = []

    while a <= abs(num):

        if a == 0:

            pass

        elif num % a == 0:

            print(a)

            divisor.append(a)

        a += 1

    print('%d의 약수의 개수 :'%num, len(divisor))
    print('약수 :',divisor)
else:
    print('%d의 약수는 모든 정수입니다.'%num)
    
    

