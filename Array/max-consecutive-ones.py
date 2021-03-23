# find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0

    # initialize max
        result = 0

        for i in range(len(nums)):

            # Reset count when 0 is found
            if (nums[i] == 0):
                count = 0

        # If 1 is found, increment count
        # and update result if count
        # becomes more.
            else:

                # increase count
                count += 1
                result = max(result, count)

        return result
