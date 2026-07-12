class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()

        for i, char in enumerate(cleaned):
            if char != cleaned[-(i+1)]:
                return False

        return True

        