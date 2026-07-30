class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        invest = prices[0]
        maxProf = 0
        for i in range(len(prices)):
            if invest > prices[i]:
                invest = prices[i]
            elif invest < prices[i]:
                if maxProf < prices[i] - invest:
                    maxProf = prices[i] - invest
        return maxProf
        

        