class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x < 0:
			return
		else:
			sign = 1
		x = abs(x)
		res = 0
		divide = 10
		digits = []
		temp = 10 * x / divide
		while(temp != 0):
			thisDigit = (x % divide) / (divide / 10)
			digits.append(thisDigit)
			divide *= 10
			temp = 10 * x / divide
		digits.reverse()
		divide = 1
		for d in digits:
			res += d * divide
			divide *= 10
		if x == sign * res:
			return True
		else:
			return False