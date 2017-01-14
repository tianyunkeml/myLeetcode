class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		def letter2num(s):
			return ord(s) - ord('A') + 1
		result = 0
		pointer = -1
		multiplier = 1
		for n in range(len(s)):
			letter = s[pointer]
			num = letter2num(letter)
			result += num * multiplier
			pointer -= 1
			multiplier *= 26
		return result
