class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		result = ''
		spare = 0
		cursor = -1
		while cursor >= -len(a) or cursor >= -len(b):
			print cursor
			digit_a = int(a[cursor]) if cursor >= -len(a) else 0
			digit_b = int(b[cursor]) if cursor >= -len(b) else 0
			res = (digit_a + digit_b + spare) % 2
			spare = (digit_a + digit_b + spare) / 2
			result = str(res) + result
			cursor -= 1
		if spare == 1:
			result = '1' + result
		return result

if __name__ == '__main__':
	print Solution().addBinary('0', '0')

        