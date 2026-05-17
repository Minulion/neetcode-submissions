class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        kList = []
        for num in nums:
            if num not in numDict:
                numDict[num] = 0
            numDict[num] += 1
        for num in range(k):
            maxKey = max(numDict, key = numDict.get)
            kList.append(max(numDict, key = numDict.get))
            del numDict[maxKey]
        return kList