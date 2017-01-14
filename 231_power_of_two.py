class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		return '{:32b}'.format(n).count('1') == 1 and n > 0