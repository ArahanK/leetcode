class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = dict() 
        for i in range(len(prices)):
            if(i <= len(prices)-2):
                max_temparray = max(prices[i+1:])
                if max_temparray > prices[i] and prices[i] not in profits.keys():
                    profits[prices[i]] = max_temparray - prices[i]
        print(profits)
        if(len(profits.values())>0):
            return max(profits.values())
        else:
            return 0


x = Solution()
print(x.maxProfit(prices=[8,6,4,3,3,2,3,5,8,3,8,2,6]))
