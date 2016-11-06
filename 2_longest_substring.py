class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        length = 0
        maxStart = 0
        maxLength = 0
        for i, c in enumerate(s):
        	if not c in s[start: start + length]:
        		length += 1
        	else:
        		if length > maxLength:
        			maxLength = length
        			maxStart = start
        		pre_trunk = s[start: start + length].rfind(c)
        		start = s[0: start + length].rfind(c) + 1
        		length = length - pre_trunk
        print s[maxStart: maxStart + maxLength]
        if length > maxLength:
        			maxLength = length
        			maxStart = start
        return maxLength

if __name__ == '__main__':
	print Solution().lengthOfLongestSubstring('abcabcdabc')

        	

