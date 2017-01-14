class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		n = n - 1
		if n < 2:
			return 0
		if n == 2:
			return 1
		testSet = range(2, max(int(n ** 0.5) + 1, 3))
		candidate = range(2, n + 1)
		for k in testSet:
			multiplier = k
			while k * multiplier <= n:
				toDel = k * multiplier
				if toDel in candidate:     # this step too time costly, better use a True|False list
					candidate.remove(toDel)
				multiplier += 1
		return len(candidate)