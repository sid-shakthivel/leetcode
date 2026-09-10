from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_stuff = defaultdict(list)
        t_stuff = defaultdict(list)

        for i in range(len(s)):
            s_stuff[s[i]].append(i)
            t_stuff[t[i]].append(i)

        return list(s_stuff.values()) == list(t_stuff.values())
