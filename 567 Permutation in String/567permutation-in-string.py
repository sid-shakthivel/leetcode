class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for letter in s1:
            s1_freq[ord(letter) - 97] += 1

        window_size = len(s1)

        for i in range(window_size):
            letter = s2[i]
            s2_freq[ord(letter) - 97] += 1

        if s1_freq == s2_freq:
            return True

        for right in range(window_size, len(s2)):
            letter = s2[right]
            prev_letter = s2[right - window_size]

            s2_freq[ord(letter) - 97] += 1
            s2_freq[ord(prev_letter) - 97] -= 1

            if s1_freq == s2_freq:
                return True

        return False