import pymysql

print('hello')

def get_book_by_name(pbookname):
    #데이터베이스 접속 관련 변수들 초기화
    host = "localhost"
    port = 3306
    database = "madang"
    username = "root"
    password = "7345"
    #접속 상태 확인
    conflag = True
    #A처리 블락 = 파이썬 예외파트에 나오나봄
    try:
        print('데이터베이스 연결 준비...')
        conn = pymysql.connect(host=host, user=username, password=password, db=database, port=port, charset='utf8')
    #mysql에 접속하는 함수, utf-8은 한글때문에(오른쪽 아래보면 파이썬도 인코딩 버전 이것이다.). 위변수가 일치하면 conn가 True 받는다.
        print('데이터베이스 연결 성공')
    except Exception as err:#try 블럭에서 예외발생이 여기로 온다.
        print('데이터베이스 연결 실패:')
        conflag = False

    #접속에 성공한다면 쿼리문 실행 코드 실행
    if conflag == True:#커서 객체 생성 cursor
        cursor = conn.cursor()
        sqlString = 'select * from book where bookname = %s;'
        res = cursor.execute(sqlString, pbookname)
        data = cursor.fetchall()
        print('data의 타입=' , type(data))

        print('{0}\t{1:<} \t{2:<} \t{3:>}'.format('bookid','bookname','publisher','price'))

        #레코드들 출력
        for rowdata in data:
            if rowdata[3] == None:
                print('{0}\t{1:<} \t{2:<} \t{3:>}'.format(rowdata[0], rowdata[1], rowdata[2], 0))
            else:
                print('{0}\t{1:<} \t{2:<} \t{3:>}'.format(rowdata[0], rowdata[1], rowdata[2], rowdata[3]))

        cursor.close()
        conn.close()


if __name__=="__main__":

    bookname = input('원하는 bookname를 입력 =>')
    get_book_by_name(bookname)