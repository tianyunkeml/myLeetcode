class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		rowIndex += 1
		myRow = [1, 1]
		if rowIndex == 0:
			return []
		elif rowIndex == 1:
			return [1]
		elif rowIndex == 2:
			return [1, 1]

		for k in range(2, rowIndex):
			nextRow = [1]
			for n in range(len(myRow) - 1):
				nextRow.append(myRow[n] + myRow[n + 1])
			nextRow.append(1)
			myRow = nextRow[:]

		return myRow
