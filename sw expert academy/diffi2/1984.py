n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    print(f"#{i+1} {round((sum(nums)/len(nums)))}")
