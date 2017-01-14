class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = s + ' '
		result = ''
		is_last_space = True
		for c in s:
			is_current_space = True if c == ' ' else False
			if is_last_space and not is_current_space:
				word = c
			elif not is_last_space and not is_current_space:
				word += c
			elif not is_last_space and is_current_space:
				word += c
				result = word + result
			else:
				pass
			is_last_space = is_current_space
		return result.strip()

if __name__ == '__main__':
	print Solution().reverseWords('  today I worked out ')