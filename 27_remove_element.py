class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		cursor = 0
		total_len = len(nums)
		while cursor < total_len:
			if nums[cursor] == val:
				del nums[cursor]
				total_len -= 1
			else:
				cursor += 1
		return len(nums)
