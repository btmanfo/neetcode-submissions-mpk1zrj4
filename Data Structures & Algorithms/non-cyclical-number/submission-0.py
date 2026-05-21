class Solution:
    def isHappy(self, n: int) -> bool:
        seenValue = set()
        while n not in seenValue:
            seenValue.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        else:
            return False
    
    def sumOfSquare(self, n):
        output = 0
        while n:
            digit = n%10
            digit = digit *digit
            output += digit
            n = n//10
        return output