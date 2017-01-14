class Solution(object):
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		sign = '+'
		str = str.strip()
		start = 0
		overflow = 'no'

		if str == '':
			return 0

		if str[0] not in '+-0123456789':
			return 0
		if str[0] in '+-':
			sign = str[0]
			start += 1

		numStr = ''
		for n in range(start, len(str)):
			if str[n] not in '0123456789':
				break
			numStr += str[n]

		if numStr == '':
			return 0
		if len(numStr) == 10:
			newStr = numStr[1:]
			if numStr[0] in '01': 
				return int(numStr) if sign == '+' else -int(numStr)
			if numStr[0] == '2':
				print int(newStr)
				print 2 ** 31 - 2 * 10 ** 9
				if sign == '+' and int(newStr) <= 2 ** 31 - 1 - 2 * 10 ** 9:
					return int(numStr) if sign == '+' else -int(numStr)
				if sign == '-' and int(newStr) <= 2 ** 31 - 2 * 10 ** 9:
					return int(numStr) if sign == '+' else -int(numStr)

			return 2 ** 31 - 1 if sign == '+' else -2 ** 31

		if len(numStr) > 10:
			return 2 ** 31 - 1 if sign == '+' else -2 ** 31

		return int(numStr) if sign == '+' else -int(numStr)

if __name__ == '__main__':
	print Solution().myAtoi('-2147483647')