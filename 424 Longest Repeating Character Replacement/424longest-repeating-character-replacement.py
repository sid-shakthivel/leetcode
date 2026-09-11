class Solution:
    from collections import defaultdict
    
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0

        freq = [0] * 26

        for right in range(len(s)):
            freq[ord(s[right]) - 65] += 1

            while (right - left + 1) - max(freq) > k:
                freq[ord(s[left]) - 65] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length