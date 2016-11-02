class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
        	if target - num in dict:
        		return (dict[target - num], i)
        	dict[num] = i

if __name__ == '__main__':
	print 'index1 = %d, index2 = %d' % Solution().twoSum((5,3,7,9,1,4), 13)