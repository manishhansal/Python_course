

# def findClosestNumber(nums):
#     dicti = {};
#     for num in nums:
#         if abs(num) not in dicti:
#             dicti[abs(num)] = num
#         elif abs(num) in dicti:
#             if dicti[abs(num)] < num:
#                 dicti[abs(num)] = num
#     return dicti[min(dicti)]

# [-10,-12,-54,-12,-544,-10000]
def findClosestNumber(nums):
    i = 0
    min = nums[i]
    for num in nums[1:]:
        if abs(num)<abs(nums[i]):
            min = num
            i+=1
        elif abs(num)==abs(nums[i]):
            if num >= nums[i]:
                min = num
                i+=1
        else:
            i+=1
    return min

nums = [2,1,1,100000]
print(findClosestNumber(nums))