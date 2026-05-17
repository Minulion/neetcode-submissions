class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s
            encoded += "¥"
        return encoded
    def decode(self, s: str) -> List[str]:
        strArr = []
        string = ""
        for char in s:
            if char == "¥":
                strArr.append(string)
                string = ""
            else:
                string += char
        return strArr
