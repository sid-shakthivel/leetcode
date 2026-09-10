class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            letter_freqencies = [0] * 26

            for char in string:
                letter_freqencies[ord(char) - ord('a')] += 1
            
            letter_freqencies = tuple(letter_freqencies)

            if letter_freqencies not in result:
                result[letter_freqencies] = []

            result[letter_freqencies].append(string)

        return list(result.values())