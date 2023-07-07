def solution(nums, dir):
    if dir == "right":
        answer = nums[0:len(nums)-1]
        answer.insert(0, nums[-1])
    else:
        answer = nums[1:len(nums)]
        answer.append(nums[0])
    return answer


print(solution([1, 2, 3], "right"))
