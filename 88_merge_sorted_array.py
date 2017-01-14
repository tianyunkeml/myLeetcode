class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		pointer = 0
		length = len(nums1)
		for num in nums2:
			print nums1
			print pointer
			if num < nums1[pointer]:
				nums1.insert(pointer, num)
				length += 1
				continue
			while(num > nums1[pointer] and pointer < length):
				pointer += 1
				if pointer == length:
					break
			nums1.insert(pointer, num)
			length += 1
		return

if __name__ == '__main__':
	nums1 = [1,2,3]
	nums2 = [2,5,6]
	Solution().merge(nums1, len(nums1), nums2, len(nums2))
	print nums1






