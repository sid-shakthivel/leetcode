from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dict = defaultdict(int)
        m_dict = defaultdict(int)

        for letter in ransomNote:
            r_dict[letter] += 1
        
        for letter in magazine:
            m_dict[letter] += 1

        for letter, freq in r_dict.items():
            if letter not in m_dict:
                return False

            if m_dict[letter] < freq:
                return False
        
        return True