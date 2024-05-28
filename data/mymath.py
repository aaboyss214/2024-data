import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time elapsed : {end - start}")
        return result
    return wrapper


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

@timer
def nCr(n, r) -> int:  #OCP violation
    """
    조합 함수
    :param n:
    :param r:
    :return: 조합 값
    """
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return int(numerator / denominator)

#파스칼

# def pas(n):
#     if n == 1:
#         return [1]
#     arr = [1]
#     for i in range(len(pas(n-1))-1):
#         arr.append(pas(n-1)[i]+pas(n-1)[i+1])
#     arr.append(1)
#     return arr
# print(pas(5))

#피보나치 0부터 시작
# def fib(n):
#     if n==0:
#         return [0]
#     if n==1:
#         return [0,1]
#     arr = fib(n-1)
#     arr.append(arr[-1]+arr[-2])
#     return arr
# print(fib(6))

