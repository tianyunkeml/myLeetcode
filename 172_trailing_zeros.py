class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		result = 0
		base = 1
		while n >= 5 ** base:
			result += (n / (5 ** base))
			base += 1
		return result