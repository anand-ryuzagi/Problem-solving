# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums) -> int:
        count = 0
        for i in range(len(nums)):
            str1 = str(nums[i])
            if len(str1) % 2 ==0:
                count +=1
                
        return count
