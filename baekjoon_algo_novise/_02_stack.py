import sys
n = int(sys.stdin.readline())
for i in range(n):
    sen = list(sys.stdin.readline().split())
    for j in sen:
        print(j[::-1], end=" ")
    print("")
