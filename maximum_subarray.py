class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        biggestsum = 0
        if len(nums)==1:
            return nums[0]
        else: 
            for i in range(len(nums)):
                number+=nums[i]
                if number < 0:
                    number = 0
                elif number > biggestsum: 
                    biggestsum = number
            if biggestsum == 0:
                biggestsum = max(nums)
        return biggestsum     
                