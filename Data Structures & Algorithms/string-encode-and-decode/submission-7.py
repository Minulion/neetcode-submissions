class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += (str(len(s)) + "#")
            encoded += s
        return encoded
    def decode(self, s: str) -> List[str]:
        strArr = []
        string = ""
        strNum = ""
        intNum = 0
        readingNum = True
        for char in s:
            if readingNum:
                if char == "#":
                    readingNum = False
                    intNum = int(strNum)
                    if intNum == 0:
                        strArr.append(string)
                        strNum = ""
                        string = ""
                        readingNum = True
                    continue
                strNum += char
            else: #not reading num, reading string
                intNum -= 1
                string += char
                if intNum <= 0:
                    strArr.append(string)
                    strNum = ""
                    string = ""
                    readingNum = True
        return strArr
