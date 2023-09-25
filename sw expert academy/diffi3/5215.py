from itertools import combinations

t = int(input())
for i in range(1, t+1):
    n, maxcal = map(int, input().split())
    material = {}
    for _ in range(n):
        a, b = map(int, input().split())
        material[b] = a
    # 키로 리스트를 만든담에 조합을 구함
    # 각 조합 1,2,3,4,5 .. n 까지 조합을 하나씩 구하는데
    # 그 조합들을 다 순회해서 sum 치고 maxcal 보다 크면 넘어감
    # 제일 큰 조합을 변수에 넣고
    # 그 다음 조합에서 sum 을 칠때 변수 sum값과 비교
    # 마지막에 변수 에서 포문으로 len만큼 간담에 각각에 value들을
    # result에 더해서 출력
    temp = []
    for j in range(1, n+1):
        templis = list(combinations(material.keys(), j))
        for k in templis:
            eq = sum(k)
            if eq >= maxcal:
                continue
            elif sum(temp) <= eq:
                tem_sum = 0
                k_sum = 0
                for a in range(len(temp)):
                    tem_sum += material[temp[a]]
                for b in range(j):
                    k_sum += material[k[b]]
                if tem_sum < k_sum:
                    temp = k
    result = 0
    for p in temp:
        result += material[p]

    print(f"#{i} {result}")
