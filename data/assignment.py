

arr = [('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

if __name__ == "__main__":
    while True:
        new = input("추가할 친구-->")
        chat = int(input("카톡 횟수-->"))
        current = len(arr)-1
        arr.append(None)
        while True:
            if arr[current][1]>chat:
                arr.insert(current+1,(new,chat))
                break
            elif current == -1:
                arr.insert(0,(new,chat))
                break
            else:
                arr[current+1]=arr[current]
                current = current -1

        print(arr)