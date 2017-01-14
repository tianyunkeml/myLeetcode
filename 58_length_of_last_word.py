class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s.strip()
		result = 0
		for c in s:
			if c != ' ':
				result += 1
			else:
				result = 0
		return result