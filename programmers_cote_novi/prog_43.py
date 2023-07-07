import time
start_time = time.time()


def solution(rsp):
    answer = ""
    for i in rsp:
        if i == "2":
            answer += '0'
        elif i == "0":
            answer += '5'
        else:
            answer += '2'
    return answer


print(solution("205"))

end_time = time.time()
print("시간: ", end_time - start_time)
