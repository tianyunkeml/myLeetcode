class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		record = [n]
		strN = str(n)
		result = n
		while result != 1:
			result = 0
			for s in strN:
				result += int(s) ** 2
			print result
			print record
			if result in record:
				return False
			else:
				record.append(result)
				strN = str(result)
		return True