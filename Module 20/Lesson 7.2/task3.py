import random


def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums = list(nums)
    nums[index] = value
    nums = tuple(nums)
    return nums, value


my_nums = 1, 2, 3, 4, 5
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums, new_rand_val = change(new_nums)
rand_val += new_rand_val
print(new_nums, rand_val)
