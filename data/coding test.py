# import random
# def get_user_choice():
#     print('가위바위보 게임을 시작합니다!')

#     while True:
#         a = input('가위, 바위, 보 중 하나를 선택하세요: ')
#         if a in ['가위','바위','보']:
#             break
#         else:
#             print('잘못된 입력입니다. 다시 선택하세요.')
#     return a
# def get_computer_choice():
#     a = random.randint(1,3)
#     if a%3==0:
#         return '가위'
#     elif a%3==1:
#         return '바위'
#     elif a%3==2:
#         return '보'
    
# def determine_winner(user_choice, computer_choice):
#     print(f'사용자: {user_choice}, 컴퓨터: {computer_choice}')
#     if user_choice == computer_choice:
#         print('결과: 무승부')
#     elif user_choice == '가위' and computer_choice == '바위':
#         print('결과: 컴퓨터 승')
#     elif user_choice == '가위' and computer_choice == '보':
#         print('결과: 사용자 승')
#     elif user_choice == '바위' and computer_choice == '가위':
#         print('결과: 사용자 승')
#     elif user_choice == '바위' and computer_choice == '보':
#         print('결과: 컴퓨터 승')
#     elif user_choice == '보' and computer_choice == '가위':
#         print('결과: 컴퓨터 승')
#     elif user_choice == '보' and computer_choice == '바위':
#         print('결과: 사용자 승')

# a = get_user_choice()
# b = get_computer_choice()
# determine_winner(a,b)

# class BankAccount:
#     def __init__(self,a=0):
#         self.money = a
#     def deposit(self,a):
#         self.money += a
#     def withdraw(self,a):
#         b = self.money - a
#         if b < 0:
#             print('잔액이 부족합니다.')
#         else:
#             self.money -= a

#     def get_balance(self):
#         return self.money

# account_1 = BankAccount(1000)
# account_1.deposit(500)
# account_1.withdraw(200)

# print(account_1.get_balance())
# account_1.withdraw(1500)

# account_2 = BankAccount()
# account_2.withdraw(200)


# class Animal:
#     def __init__(self,name):
#         self.name = name

# class Dog(Animal):
#     def speak(self):
#         return '{}는 멍멍'.format(self.name)

# class Cat(Animal):
#     def speak(self):
#         return '{}는 야옹'.format(self.name)
        
# dog = Dog('절미')
# cat = Cat('동글이')
# print(dog.speak())
# print(cat.speak())

class Book():
    def __init__(self, book, name):
        self.book = book
        self.name = name

class Library():
    def __init__(self):
        self.containor = {}

    def add_book(self,book):
        if book in self.containor.keys():
            self.containor[book][2] += 1
        else:
            self.containor[book]=[book.book, book.name, 1]

    def print_books(self):
        print('---도서관 소장 도서 목록---')
        for  book in self.containor.values():
            print(f'제목: {book[0]}, 작가: {book[1]}, 찬여 책 개수: {book[2]}')
        print('---------------------------')

    def borrow_book(self,bookname):
        for i in self.containor.values():
            if i[0] == bookname:
                book=i
                break
        if book[2] > 0:
            print(f"책 '{book[0]}'을 대출하였습니다.")
            book[2] -= 1
        else:
            print('현재 책이 없습니다.')

    def return_book(self,bookname):
        for i in self.containor.values():
            if i[0] == bookname:
                book=i
                break
        book[2] += 1
        print(f"책 '{book}'을 반납하였습니다.")
    
        

book1 = Book('파이썬 코딩도장', '남재윤')
book2 = Book('명품 JAVA Programing', '황기태, 김효수')

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book1)
library.add_book(book2)
library.add_book(book1)
library.add_book(book2)

library.print_books()

library.borrow_book('파이썬 코딩도장')
library.borrow_book('파이썬 코딩도장')
library.borrow_book('파이썬 코딩도장')
library.borrow_book('파이썬 코딩도장')
library.print_books()

library.return_book('파이썬 코딩도장')
library.print_books()

