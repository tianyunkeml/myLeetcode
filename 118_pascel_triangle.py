class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		result = []
		if numRows == 0:
			return []
		elif numRows == 1:
			return [[1]]
		elif numRows == 2:
			return [[1], [1, 1]]
		result = [[1], [1, 1]]
		for k in range(2, numRows):
			newOne = [1]
			lastOne = result[-1]
			for n in range(len(lastOne) - 1):
				newOne.append(lastOne[n] + lastOne[n + 1])
			newOne.append(1)
			result.append(newOne[:])
		return result

