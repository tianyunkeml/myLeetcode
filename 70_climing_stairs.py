class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 1:
			return 1
		if n == 2:
			return 2
		result = Solution().climbStairs(n - 1) + Solution().climbStairs(n - 2)
		return result

if __name__ == '__main__':
	print Solution().climbStairs(5)