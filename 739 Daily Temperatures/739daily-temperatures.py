class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
                
            while len(stack) > 0 and temp > stack[-1][0]:
                removed = stack.pop()
                res[removed[1]] = i - removed[1]
            
            stack.append((temp, i))
                
        return res