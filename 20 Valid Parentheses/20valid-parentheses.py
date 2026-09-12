class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for letter in s:
            if letter in bracket_map.values():
                stack.append(letter)
            else:
                if len(stack) == 0 or (stack.pop() != bracket_map[letter]):
                    return False

        return True if len(stack) == 0 else False