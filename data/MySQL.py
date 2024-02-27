"""
1번 문제 답
"""
# import pymysql
# conn = pymysql.connect(host="localhost",
#                        user = "root",
#                        password="7345",
#                        database="madang",
#                        charset="utf8")
# try:
#     cursor = conn.cursor()
#     # 아래 코드 수정
#     selectBooksql = "select name, sum(saleprice) from customer, orders where customer.custid = orders.custid group by name"
#     cursor.execute(selectBooksql)
#     books = cursor.fetchall()
#     for book in books:
#         print(book)
# except Exception as e:
#     print(f"에러가 발생함: {e}")
#     conn.rollback()
# finally:
#     cursor.close()
#     conn.close()
"""
2번 문제 답"
"""
import pymysql
conn = pymysql.connect(host="localhost",
                       user = "root",
                       password="7345",
                       database="madang",
                       charset="utf8")
try:
    cursor = conn.cursor()
    # 아래 코드 수정
    selectBooksql = "select name, avg(saleprice) from orders od1, customer where (select avg(saleprice) from orders od2 where od1.custid = od2.custid)>(select avg(saleprice) from orders) and od1.custid = customer.custid group by customer.name;"
    cursor.execute(selectBooksql)
    books = cursor.fetchall()
    for book in books:
        print(book)
except Exception as e:
    print(f"에러가 발생함: {e}")
    conn.rollback()
finally:
    cursor.close()
    conn.close()