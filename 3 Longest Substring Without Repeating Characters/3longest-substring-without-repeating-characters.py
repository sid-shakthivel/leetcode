from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_map = defaultdict()

        max_ss_length = 0
        left = 0

        for right in range(len(s)):
            letter = s[right]

            if letter not in letter_map:
                letter_map[letter] = right
            else:
                left = max(left, letter_map[letter] + 1)
                letter_map[letter] = right

            max_ss_length = max(max_ss_length, right - left + 1)

        return max_ss_length