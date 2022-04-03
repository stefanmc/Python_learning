"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""
from typing import List


# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         for i in range(len(nums)):
#             for each in range(i+1,len(nums)):
#                 if nums[i] + nums[each] == target:
#                     return [i,each]
# solution = Solution()
# nums = [3,3]
# target = 6
# result = solution.twoSum(nums,target)
# print(result)


class Solution():
    def twoSum(self, nums: list, target: int) -> list:
        dct = {}
        for i,n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp],i]
            else:
                dct[n] = i

solution = Solution()
nums = [2,15,11,7]
target = 9
result = solution.twoSum(nums,target)
print(result)


