class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		length = len(strs)
		if length == 0:
			return ''
		if length == 1:
			return strs[0]
		cmstr = strs[0]
		for string in strs[1:]:
			if string == '' or cmstr == '':
				return ''
			sign = 1
			for i in range(min(len(cmstr), len(string))):
				if cmstr[i] != string[i]:
					sign = 0
					break
			if sign == 1:
				i += 1
			cmstr = cmstr[:i]
		return cmstr

if __name__ == '__main__':
	print Solution().longestCommonPrefix(['', 'b'])

