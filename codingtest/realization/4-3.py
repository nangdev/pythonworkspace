ans = list(input())
result = 8
if int(ans[1])+2 > 8:
    result -= 2
else:
    if ord(ans[0])+1 > ord('h'):
        result -= 1
    elif ord(ans[0])-1 < ord('a'):
        result -= 1
if int(ans[1])-2 < 1:
    result -= 2
else:
    if ord(ans[0])+1 > ord('h'):
        result -= 1
    elif ord(ans[0])-1 < ord('a'):
        result -= 1
if ord(ans[0])+2 > ord('h'):
    result -= 2
else:
    if int(ans[1])+1 > 8:
        result -= 1
    elif int(ans[1])-1 < 1:
        result -= 1
if ord(ans[0])-2 < ord('a'):
    result -= 2
else:
    if int(ans[1])+1 > 8:
        result -= 1
    elif int(ans[1])-1 < 1:
        result -= 1
print(result)
