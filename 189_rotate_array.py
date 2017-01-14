class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		copy = nums[-k - 1:]
		for i in reversed(range(len(nums))):
			newInd = (i - k) % len(nums)
			if len(nums) - newInd <= k:
				nums[i] = copy[newInd - len(nums)]
			else:
				nums[i] = nums[newInd]


