class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0

        for i in digits:
            digit = digit*10 + i
        print(digit)
        digit = digit +1
        res = []

        while digit:
            temp = digit% 10
            res.append(temp)
            digit = digit //10
        reversRes = []
        for i in range(len(res)-1, -1, -1):
            reversRes.append(res[i])
        return reversRes