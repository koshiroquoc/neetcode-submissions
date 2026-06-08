class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0
        profit = 0
        for right in range (1,len(prices)):
            if prices[left] > prices[right]:
                left = right 
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
            ans = max(ans,profit)
        return ans