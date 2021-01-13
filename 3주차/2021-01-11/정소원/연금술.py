N, M = int(input()), int(input())
nums = list(map(int, input().split()))

nums.sort()
complements = [M-nums[i] for i in range(len(nums))]
#print(nums, complements)

i, res = 0, 0
while True:
    if i == N or nums[i] >= M/2:
        break
    if complements[i] in nums:
        res += 1
    i += 1
print(res)
