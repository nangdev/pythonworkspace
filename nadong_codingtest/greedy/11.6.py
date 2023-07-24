def solution(food_times, k):
    time = 0
    while sum(food_times) != 0:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue

            if time == k:
                return i+1

            food_times[i] -= 1
            time += 1

    return -1


print(solution([3, 1, 2], 5))
