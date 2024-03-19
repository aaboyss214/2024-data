def fac(a):
    data = 1
    for i in range(1,a+1):
        data = data*i
    return data

def comb(n , m):
    return int(fac(m)/(fac(m-n)*fac(n)))

if __name__=='__main__':   
    n, m = map(int, input().split())
    print(comb(n , m))

