class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        char_set = set()
        left = 0

        for right, num in enumerate(s):

            # if not dupe, add to set
            if num not in char_set:
                char_set.add(num)
                max_len = max(max_len, right - left + 1)

            # shrink window from left until no more dupe
            else: 
                while (num in char_set):
                    char_set.remove(s[left])
                    left += 1
                char_set.add(num)

        return max_len
        