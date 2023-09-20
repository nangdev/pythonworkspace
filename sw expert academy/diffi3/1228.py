for t in range(1, 11):
    colen = int(input())
    code = input().split()
    dirlen = int(input())
    dirlis = input().split()
    dir = []
    for i in range(1, len(dirlis)):
        if dirlis[i] == 'I':
            for k in range(int(dir[1])):
                code.insert(int(dir[0])+k, dir[k+2])
            dir.clear()
        elif dirlis[i] == dirlis[-1]:
            dir.append(dirlis[i])
            for k in range(int(dir[1])):
                code.insert(int(dir[0])+k, dir[k+2])
        else:
            dir.append(dirlis[i])

    print(f"#{t}", end=" ")
    for l in range(10):
        print(code[l], end=" ")
    print()
