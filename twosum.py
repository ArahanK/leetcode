class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = dict()
        numbersarray = []
        for i in range(len(nums)):
            if target-nums[i] in numbers: 
                return [numbers[target-nums[i]], i]
            else:
                numbers[nums[i]]=i
            