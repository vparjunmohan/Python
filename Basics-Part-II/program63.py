'''Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not. 
For example, given [1, 5, 11, 5] and k = 16, return true since 11 + 5 is 16.
Sample Output:
True
True
True
False'''


def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))
