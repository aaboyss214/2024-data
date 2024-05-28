#1
# def down(i):
#     global index, answer
#     index = [index[0]+1,index[1]]
#     answer[index[0]][index[1]] = i

# def move(i):
#     global index, answer
#     a,b = index
#     index = [index[0]-1,index[1]+1]
#     if index[0]==-1:
#         index[0]=number-1
#     if index[1]==number:
#         index[1]=0


#     if answer[index[0]][index[1]]!=0:
#         index = [a,b]
#         down(i)
#     else:
#         answer[index[0]][index[1]] = i


# number = int(input())
# answer = [[0]*number for _ in range(number)]
# index = [0,number//2]
# answer[index[0]][index[1]] = 1
# for i in range(2,number*number+1):
#     move(i)
# for i in answer:
#     print(i)



#2
# while True:
#     number = int(input('양의 홀수 정수 입력: '))
    
#     if number % 2 == 0:
#         print('프로그램 종료')
#         break

#     answer = [[0]*number for _ in range(number)]
#     index=[0,number//2]
#     answer[index[0]][index[1]] = 1
#     for i in range(2,number**2+1):
#         a,b = index
#         index=[index[0]-1,index[1]+1]
#         if index[0] == -1:
#             index[0]=number-1
#         if index[1] == number:
#             index[1]=0
#         if answer[index[0]][index[1]]!=0:
#             index=[a+1,b]
#             answer[index[0]][index[1]]=i
#         else:
#             answer[index[0]][index[1]]=i
#     for i in answer:
#         for j in i:
#             print('{:<3d}'.format(j),end='')
#         print()
#     print()

#     with open('exam.txt','a') as file:
#         for i in answer:
#             for j in i:
#                 file.write('{:<3d}'.format(j))
#             file.write('\n')
#         file.write('\n')

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n*factorial(n-1)

# number = int(input('양의 정수 입력: '))
# arr='(x+y)**'
# arr += str(number) + '=' + 'x' + str(number) + '+' + str(int(factorial(number)/(factorial(number-1)*factorial(1)))) + 'x' + str(number-1) + 'y' + '+'

# for i in range(2,number-1):
#     k = int(factorial(number)/(factorial(number-i)*factorial(i)))
#     a = number-i
#     b = i
#     arr += str(k)+'x'+str(a)+'y'+str(b)+'+'
# arr += str(int(factorial(number)/(factorial(1)*factorial(number-1)))) + 'x'  + 'y' + str(number-1) + '+' +'y' + str(number)
# print(arr)

# def pascal(n):
#     if n == 0:
#         return [1]
#     if n == 1:
#         return [1,1]
#     arr = [1]
#     for i in range(n-1):
#         k = pascal(n-1)[i] + pascal(n-1)[i+1]
#         arr.append(k)
#     arr.append(1)
#     return arr

# print(' '*2,end='')
# for i in pascal(4):
#     print('{:<3d}'.format(i),end='')
# print()
# for i in pascal(5):
#     print('{:<3d}'.format(i),end='')

def generate_pascals_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    max_width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = "   ".join(map(str, row))
        print(row_str.center(max_width))

n = 10  # 원하는 파스칼 삼각형의 높이
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)
