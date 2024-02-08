'''
def factorial(number) -> int:
    """
    factorial by repetition
    :param number: number (int)
    :return: factorial result (int)
    """
    result = 1
    for i in range(1, number+1):
        result = result*i
    return result
'''

def factorial(number) -> int:
    """
    factorial by recursion
    :param number: number (int)
    :return: factorial (int)
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def nCr(n, r) -> int:
    """
    조합 함수
    :param n:
    :param r:
    :return: 조합 값
    """
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return int(numerator / denominator)