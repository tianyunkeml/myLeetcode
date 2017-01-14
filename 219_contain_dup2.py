class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		record = {}
		for n in range(len(nums)):
			strN = str(nums[n])
			if strN not in record:
				record[strN] = n
			else:
				if n - record[strN] <= k:
					return True
				record[strN] = n
		return False
