class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		digits.reverse()
		result = []
		overflow = 1
		for d in digits:
			if d == 9 and overflow == 1:
				d = 0
				overflow = 1
			else:
				d = d + overflow
				overflow = 0
			result.append(d)
		if overflow == 1:
			result.append(1)
		result.reverse()
		return result

if __name__ == '__main__':
	print Solution().plusOne([5,6,9,9,9])
