class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		length = len(matrix)
		center = 1.0 * length / 2 + 0.5
		for h in range(0, int(center)):
			for w in range(0, int(center - 0.5)):
				copy = matrix[h][w]
				matrix[h][w] = matrix[length - w - 1][h]
				matrix[length - w - 1][h] = matrix[length - h - 1][length - w - 1]
				matrix[length - h - 1][length - w - 1] = matrix[w][length - h - 1]
				matrix[w][length - h - 1] = copy



