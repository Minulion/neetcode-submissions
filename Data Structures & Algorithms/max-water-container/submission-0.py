class Solution:
    def maxArea(self, height: list[int]) -> int:


        # area calculation: min(heights) * (right-left)
        # therefore, for a shorter line, its max area is the furthest line away
        # so you can safely move the shorter line up, since you know its max area

        # then, what to do if they are equal? move both because either way, we have the max area for that height?

        # two pointers, start on both ends
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            print(area)
            if area > max_area:
                max_area = area
            
            #three cases: left smaller, right smaller, equal
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return max_area



        