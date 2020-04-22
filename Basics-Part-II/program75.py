'''Write a Python program to find the starting and ending position of a given value in a given array of integers, sorted in ascending order. 
If the target is not found in the array, return [0, 0].
Input: [5, 7, 7, 8, 8, 8] target value = 8
Output: [0, 5]
Input: [1, 3, 6, 9, 13, 14] target value = 4
Output: [0, 0]
Sample Output:
[0, 5]
[0, 0]'''


def search_Range(array_nums, target_val):
    result_arra = []
    start_pos = 0
    end_pos = 0
    for i in range(len(array_nums)):
        if target_val == array_nums[i] and start_pos == -1:
            start_pos = i
            end_pos = i
        elif target_val == array_nums[i] and start_pos != -1:
            end_pos = i
    result_arra.append(start_pos)
    result_arra.append(end_pos)
    return result_arra


print(search_Range([5, 7, 7, 8, 8, 8], 8))
print(search_Range([1, 3, 6, 9, 13, 14], 4))
print(search_Range([5, 7, 7, 8, 10], 8))
