n = int(input())
rs = []


def dice(num):
    if num == n:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, 7):
        rs.append(i)
        dice(num+1)
        rs.pop()


dice(0)
