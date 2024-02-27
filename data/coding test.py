T = int(input())

arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for test_case in range(1, T+1):
    str_ = input()
    bin_str = str()
    temp = str()
    ascii = str()
    for i in str_:
        binary = bin(arr.index(i))
        bin_str += "0"*(8 -len(binary)) + binary[2:]

    for j in bin_str:
        temp += j
        if len(temp)%8 == 0:
            ascii += chr(int(temp,2))
            temp = str()
    print(f'#{test_case} {ascii}')







