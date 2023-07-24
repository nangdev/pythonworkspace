# n = input()
# zerocount = n.count('0')
# onecount = n.count('1')
# counter = n[0]
# result = 0

# if zerocount > onecount:
#     for i in n:
#         if counter != i:
#             result += 1
#             counter = i

# elif zerocount < onecount:

# elif zerocount == onecount:

# 100101
# 입력
S = input()

# 초기화
num = int(S[0])
zero_count = 0
one_count = 0

# 계산
for i in range(len(S)):
    present = int(S[i])
    if num == present:
        continue
    elif num == 0:
        zero_count += 1
        num = present
    else:
        one_count += 1
        num = present

result = min(zero_count, one_count)
print(result)
