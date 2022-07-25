class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid+ 1
            else:
                right = mid
        return left
