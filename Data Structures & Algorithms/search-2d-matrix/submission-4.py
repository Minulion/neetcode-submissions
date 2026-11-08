class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # first, binary search to find the correct row
        # then binary search within the row to find the col coord

        left = 0
        right = len(matrix) - 1

        #len 6, last index 5
        #midpoint is either 2 or 3 (check 2)

        #len 5, last index 4
        #mipoint is 2

        while left < right:
            midpoint = (left + right + 1) // 2

            if matrix[midpoint][0] <= target:
                left = midpoint
            else:
                right = midpoint - 1

        row = left

        left = 0
        right = len(matrix[row]) - 1

        if right == 0:
            return (target == matrix[row][0])

        while left <= right:
            midpoint = (left+right)//2

            if matrix[row][midpoint] < target:
                left = midpoint + 1
            elif matrix[row][midpoint] > target:
                right = midpoint - 1
            else:
                return True
        return False