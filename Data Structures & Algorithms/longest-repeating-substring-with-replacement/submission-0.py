class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I get to replace k elements
        # a window is valid if the frequency of the most common character = len - k
        from collections import defaultdict

        longest = 1
        left = 0
        window_counts = defaultdict(int)

        for right, char in enumerate(s):
            window_counts[char] += 1

            window_len = right - left + 1

            # can you convert this window into all repeating chars?
            # if no, make it so. 
            while max(window_counts.values()) < window_len - k:
                window_counts[s[left]] -= 1
                left += 1
                window_len -= 1
            longest = max(longest, window_len)
        
        return longest

        