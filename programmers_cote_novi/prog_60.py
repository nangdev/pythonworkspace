def solution(string):
    answer = ''
    for i in string:
        if i in answer:
            continue
        answer += i
    return answer


print(solution("people"))
