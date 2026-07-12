class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)

        longest = 0

        #only count sequence from valid start points
        #valid start if num - 1 is not in set

        for num in numset:
            if num - 1 not in numset:
                current = num
                while current + 1 in numset:
                    current = current + 1
                if current - num + 1 > longest:
                    longest = current - num + 1
        
        return longest


        
        