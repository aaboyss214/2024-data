test_case = int(input())

grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0',]
for i in range(test_case):
    student_number, student = map(int, input().split())
    arr1 = []
    for j in range(student_number):
        a,b,c = map(int , input().split())
        arr1.append(a*0.35+b*0.45+c*0.2)
    scores = arr1[student-1]
    arr1.sort(reverse=True)
    index_ = arr1.index(scores)
    n = int(student_number/10)
    print(f'#{i+1} {grade[index_//n]}')
