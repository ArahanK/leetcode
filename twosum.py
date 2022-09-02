class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = dict()
        numbersarray = []
        for index, count in enumerate(nums):
            sub = target-count 
            numbers[index] = sub
            if sub in nums:
                thisindex = index
                thissub = sub
                numbersarray+=thisindex
            if nums[index]==thissub and index!=thisindex:
                numbersarray+=index
            sub = 0

        return numbersarray
                