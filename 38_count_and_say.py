class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		result = ''
		n_str = str(n)
		current_n = ''
		current_length = 0
		for c in n_str:
			if c != current_n:
				if current_n != '':
					result = result + str(current_length) + current_n
				current_n = c
				current_length = 1
			else:
				current_length += 1
		result = result + str(current_length) + current_n
		current_n = c
		current_length = 0

		return int(result)

if __name__ == '__main__':
	print Solution().countAndSay(211344)