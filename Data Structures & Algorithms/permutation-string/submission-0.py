class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # intuition: check sliding window for counts of s1
        from collections import Counter
        from collections import defaultdict

        s1_counts = Counter(s1)
        left = 0
        window_counts = defaultdict(int) # empty dict, to populate

        for right, char in enumerate(s2): # go thru each char in s2
            if right - left + 1 > len(s1): # if window exceeds s1 size, shrink by 1
                window_counts[s2[left]] -= 1
                if window_counts[s2[left]] == 0:
                    del window_counts[s2[left]]
                left += 1

            window_counts[char] += 1

            if window_counts == s1_counts:
                return True
        
        return False