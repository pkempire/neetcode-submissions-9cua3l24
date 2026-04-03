class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf') 
        res = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif price-lowest > res:
                res = price-lowest 
        return res        

