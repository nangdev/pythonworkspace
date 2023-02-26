def solution(cip, code):
    answer = ""
    for i in range(len(cip)):
        if (i+1) % code == 0:
            answer += cip[i]
    return answer


print(solution("dfjardstddetckdaccccdegk", 4))
