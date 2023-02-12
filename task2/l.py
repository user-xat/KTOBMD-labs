# L. Разные четные
n = input()
nums = list(map(int, input().split()))
sum_even_index = 0
for i in range(1, len(nums), 2):
    sum_even_index += nums[i]

sum_even_number = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        sum_even_number += nums[i]

print(sum_even_index, sum_even_number)
