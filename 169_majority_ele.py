class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		record = {}
		for n in nums:
			nStr = str(n)
			if nStr in record:
				record[nStr] += 1
			else:
				record[nStr] = 1
		for k, v in record.items():
			if v > len(nums) / 2:
				return int(k)
