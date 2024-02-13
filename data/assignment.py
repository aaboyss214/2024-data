## 함수 선언 부분 ## 
def printPoly(t_x, p_x):
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xVal, t_x, p_x):
    retValue = 0

    for i in range(len(p_x)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수
        retValue += coef * xValue ** term

    return retValue


## 전역 변수 선언 부분 ## 
# tx = [300, 20, 0]
# px = [7, -4, 5]
tx_px = [[300, 20, 0], [7, -4, 5]]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(tx_px[0], tx_px[1])
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, tx_px[0], tx_px[1])
    print(pxValue)
