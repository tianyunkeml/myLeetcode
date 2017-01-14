class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		has_dot = False
		has_e = False
		has_num = False
		s = s.strip()
		for c in s:
			if c in '0123456789':
				has_num = True
			if c not in '-+.e0123456789':
				return False
			if c in '.':
				if has_dot == True:
					return False
				has_dot = True
			if c in 'e':
				if has_e == True:
					return False
				has_e = True
		if has_num == False:
			return False
		if '+' in s:
			ind = s.index('+')
			if ind != 0 and (s[ind - 1] != 'e' or ind == len(s) - 1 or s[ind + 1] == 'e'):
				return False
			ind = s.rfind('+')
			if ind != 0 and (s[ind - 1] != 'e' or ind == len(s) - 1 or s[ind + 1] == 'e'):
				return False
		if '-' in s:
			ind = s.index('-')
			if ind != 0 and (s[ind - 1] != 'e' or ind == len(s) - 1 or s[ind + 1] == 'e'):
				return False
			ind = s.rfind('-')
			if ind != 0 and (s[ind - 1] != 'e' or ind == len(s) - 1 or s[ind + 1] == 'e'):
				return False
		if '.' in s:
			ind = s.index('.')
			if ((ind != 0 and s[ind - 1] not in '0123456789') or ind == 0) and ((ind != len(s) - 1 and s[ind + 1] not in '0123456789') or ind == len(s) - 1):
				return False
		if 'e' in s:
			ind = s.index('e')
			if ind == 0 or ind == len(s) - 1:
				return False
			if s[ind - 1] not in '.0123456789' or s[ind + 1] not in '+-.0123456789':
				return False
		if '.' in s and 'e' in s:
			if s.index('.') > s.index('e'):
				return False


		return True

if __name__ == '__main__':
	print Solution().isNumber(' 005047e+6')
