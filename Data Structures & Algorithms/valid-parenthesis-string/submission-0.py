class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] == '(' and s[r] == ')':
                l +=1
                r -=1
            elif s[l] == '*' and s[r] == ')':
                l+=1
                r-=1
            elif s[l] == '(' and s[r] == '*':
                l+=1
                r-=1
            elif s[l] == '*' and s[r] == '*':
                l+=1
                r-=1
            else:
                return False
        return True