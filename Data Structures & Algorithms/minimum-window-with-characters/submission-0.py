class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initial idea: expand window to right until substring is found
        # then shrink until can't anymore
        # AAABACABC
        from collections import Counter

        target_counts = Counter(t)
        st_counts = {} # keep track of counts of characters from target
        for letter in target_counts:
            st_counts[letter] = 0

        left = 0
        substring = False
        min_window = ""

        # key issue: how to know if window is substring?
        # every value in st_counts >= equivalent in target_counts
        # O(n) to check

        for right, char in enumerate(s):
            if char in st_counts: # update target chars
                st_counts[char] += 1

                #check substring
                if substring == False and st_counts[char] == target_counts[char]:
                    substring = all(st_counts[k] >= target_counts[k] for k in target_counts)
                        

                if substring == True: # if substring, shrink as much as possible

                    # if left character can be cut off, cut it
                    while ((s[left] not in st_counts) or (st_counts[s[left]] > target_counts[s[left]])):
                        if s[left] in st_counts:
                            st_counts[s[left]] -= 1
                        left += 1

                    if min_window == "":
                        min_window = s[left:right+1]

                    if right - left + 1 < len(min_window):
                        min_window = s[left:right+1]

        return min_window