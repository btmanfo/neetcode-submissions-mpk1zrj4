class Solution:
    def romanToInt(self, s: str) -> int:
        romanLetter = {"I": 1, "V":5, "X":10, "L":50, "C":100,
                        "D":500, "M":1000}
        res = 0
        for i in range(len(s)):
            if i+1< len(s) and romanLetter[s[i]] < romanLetter[s[i+1]]:
                res -= romanLetter[s[i]]
            else:
                res += romanLetter[s[i]]
        return res