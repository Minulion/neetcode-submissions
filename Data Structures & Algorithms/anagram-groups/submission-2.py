class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        anaArray = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in wordDict:
                wordDict[sortedWord] = []
            wordDict[sortedWord].append(word)

        for key in wordDict:
            anaArray.append(wordDict[key])
        return anaArray
        



        