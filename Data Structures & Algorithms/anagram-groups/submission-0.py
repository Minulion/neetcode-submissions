class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaArray = []
        for word in strs:
            anagrams = []
            if any(word in arr for arr in anaArray):
                continue
            for cmpWord in strs:
                if word in anaArray:
                    continue
                if len(cmpWord) == len(word):
                    if self.isAnagram(word, cmpWord):
                        anagrams.append(cmpWord)
                else:
                    continue
            anaArray.append(anagrams)
        return anaArray
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        tDict = {}
        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1
        return sDict == tDict



        