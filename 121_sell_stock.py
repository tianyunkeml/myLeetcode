class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) == 0:
			return 0
		profit = 0
		minPrice = prices[0]
		for n in range(1, len(prices)):
			if prices[n] < minPrice:
				minPrice = prices[n]
			elif prices[n] - minPrice > profit:
				profit = prices[n] - minPrice
		return profit
        