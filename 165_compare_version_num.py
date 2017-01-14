class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		start1 = 0
		start2 = 0
		prevLen1 = 0
		prevLen2 = 0
		versionCopy1 = version1[:]
		versionCopy2 = version2[:]
		while start1 != None or start2 != None:
			print start1
			print start2
			if start1 == None:
				num1 = 0
			elif '.' in versionCopy1[start1:]:
				ind1 = versionCopy1[start1:].index('.') + prevLen1
				num1 = int(versionCopy1[start1: ind1])
				prevLen1 += ind1 + 1 - start1
				start1 = ind1 + 1
			else:
				num1 = int(versionCopy1[start1:])
				start1 = None
			if start2 == None:
				num2 = 0
			elif '.' in versionCopy2[start2:]:
				ind2 = versionCopy2[start2:].index('.') + prevLen2
				print 'dsfd' + str(ind2)
				num2 = int(versionCopy2[start2: ind2])
				prevLen2 += ind2 + 1 - start2
				start2 = ind2 + 1
			else:
				num2 = int(versionCopy2[start2:])
				start2 = None
			if num1 > num2:
				return 1
			if num2 > num1:
				return -1
		return 0
