n = int(input())
li = []
while (n > 0):
    direct = list(map(str, input().split()))

    if len(direct) == 2:  # push
        li.append(int(direct[1]))
        n -= 1
        continue

    elif direct[0] == "pop":  # pop
        if len(li) == 0:
            print(-1)
            n -= 1
            continue
        print(li.pop())
        n -= 1
        continue

    elif direct[0] == "size":  # size
        print(len(li))
        n -= 1
        continue

    elif direct[0] == "show":
        print(li)

    elif direct[0] == "empty":  # empty
        if len(li) == 0:
            print(1)
        else:
            print(0)
        n -= 1
        continue

    elif direct[0] == "top":  # top
        if len(li) == 0:
            print(-1)
            n -= 1
            continue
        print(li[-1])
        n -= 1
        continue
