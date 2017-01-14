class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def findIntersect(l1, r1, l2, r2):
            return max(0, min((r1 - l2), (r2 - l1), (r1 - l1), (r2 - l2)))
        return (C - A) * (D - B) + (G - E) * (H - F) - findIntersect(A, C, E, G) * findIntersect(B, D, F, H)