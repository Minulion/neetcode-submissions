class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaArray = []
        for word in strs:
            wordDict = self.letterDict(word)
            anagrams = []
            if any(word in arr for arr in anaArray):
                continue
            for cmpWord in strs:
                if word in anaArray:
                    continue
                if len(cmpWord) == len(word):
                    if wordDict == self.letterDict(cmpWord):
                        anagrams.append(cmpWord)
                else:
                    continue
            anaArray.append(anagrams)
        return anaArray
    def letterDict(self, s: str) -> dict:
        sDict = {}
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        return sDict



        