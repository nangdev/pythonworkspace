def solution(arr):
    answer = []
    answer.append(max(arr))
    answer.append(arr.index(max(arr)))
    return answer


print(solution([1, 8, 3]))
