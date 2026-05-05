class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        i=0
        j=1
        max_profit=0
        while j<len(prices):
            if prices[i]<prices[j]:
                max_profit=max(prices[j]-prices[i],max_profit)
            else:
                i=j
            j+=1
        return max_profit
            