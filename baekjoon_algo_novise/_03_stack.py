import sys
n = int(sys.stdin.readline())
for i in range(n):
    sum = 0
    pro = list(sys.stdin.readline())
    for j in pro:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")
