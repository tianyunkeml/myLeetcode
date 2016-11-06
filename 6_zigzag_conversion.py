class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows == 1:
			return s
		container = ['' for i in range(numRows)]
		pointer = 0
		transition = 1
		result = ''
		for ind in range(len(s)):
			container[pointer] += s[ind]
			pointer += transition
			if pointer == numRows - 1:
				transition = -1
			if pointer == 0:
				transition = 1
		for frag in container:
			result = result + frag
		return result

if __name__ == '__main__':
	print Solution().convert("PAYPALISHIRING", 3)

