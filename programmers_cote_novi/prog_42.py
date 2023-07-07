def solution(string):
    answer = ""
    for i in string:
        if (i.isupper()):
            answer += i.lower()
        else:
            answer += i.upper()
    return answer


print(solution("cccCCC"))
