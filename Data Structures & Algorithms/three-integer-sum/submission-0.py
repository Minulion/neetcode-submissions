class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # three numbers from list with unique indices that add up to 0
        # not only unique indices, but unique numbers
        # given x, y + z = -x

        nums.sort()
        
        # set of tuples to store valid triplets! (NOT indices)
        triplets = set()

        # iterate through nums
        # for each num, search for its complement with two pointers

        # error: starting nums can have multiple matches
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            comp = -num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == comp: 
                    if left == i:
                        left += 1
                    elif right == i:
                        right -= 1
                    else:
                        triple = (num, nums[left], nums[right])
                        triplets.add(triple)
                        left += 1
                        right -= 1
                elif total < comp:
                    left += 1
                else:
                    right -= 1

        return list(list(x) for x in triplets)


    