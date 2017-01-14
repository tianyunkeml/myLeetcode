class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		def maxRob(houses):
			if len(houses) == 1:
				return houses[0]
			if len(houses) == 2:
				return max(houses[0], houses[1])
			return max(maxRob(houses[1:]), houses[0] + maxRob(houses[2:]))
		return maxRob(nums)