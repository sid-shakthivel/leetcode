from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(int)

        for i in range(len(s)):
            letter = s[i]
            chars[letter] += 1
        
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        
        return -1