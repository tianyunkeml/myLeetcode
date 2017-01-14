class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		def num2letter(num):
			return chr(num + ord('A') - 1)

		result = ''
		digit = (n - 1) % 26 + 1
		remain = (n - 1) / 26
		result = num2letter(digit) + result
		while remain != 0:
			digit = (remain - 1) % 26 + 1
			result = num2letter(digit) + result
			remain = (remain - 1) / 26
		return result