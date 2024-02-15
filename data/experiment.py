
a = 2
def change():
    global a
    a=3
def b():
    global a
    print(a)
if __name__=="__main__":
    b()
    change()
    b()