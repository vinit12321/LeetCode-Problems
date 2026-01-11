class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=float('inf')
        max1=float('-inf')

        for i in range(len(prices)):
            min1=min(min1,prices[i])
            max1=max(max1,prices[i]-min1)
        return max1