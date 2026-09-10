class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        window_size = k

        num_vowels = 0
        for i in range(window_size):
            if s[i] in vowels:
                num_vowels += 1

        max_num_vowels = num_vowels

        for right in range(window_size, len(s)):
            letter = s[right]
            last_letter = s[right - window_size]

            if letter in vowels:
                num_vowels += 1
            
            if last_letter in vowels:
                num_vowels -= 1

            max_num_vowels = max(max_num_vowels, num_vowels)

        return max_num_vowels