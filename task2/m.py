# M. Равен сумме соседей
n = input()
nums = list(map(int, input().split()))
for x in range(1, len(nums)-1):
    if nums[x] == nums[x-1] + nums[x+1]:
        print(nums[x], end=" ")
print()
