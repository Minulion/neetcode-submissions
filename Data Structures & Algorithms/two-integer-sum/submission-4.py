class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        for i in range(len(nums)):
            num = nums[i]
            if target - num in numDict:
                if num == target - num and numDict[num] == 1:
                    continue
                return [i, nums.index(target - num, i+1)]


        