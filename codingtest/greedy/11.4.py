from itertools import combinations

n = int(input())
lis = list(map(int, input().split()))

result = lis.copy()  # 새로운 리스트 생성하여 결과 저장

for i in range(2, n+1):
    comb = list(map(sum, combinations(lis, i)))
    result.extend(comb)  # 결과를 result 리스트에 추가

lis = result  # 결과를 lis 리스트에 대입

for i in range(1, len(lis)):
    if i not in lis:
        print(i)
        break
