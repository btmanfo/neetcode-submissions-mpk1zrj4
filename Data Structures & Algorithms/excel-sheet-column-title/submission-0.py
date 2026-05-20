class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        # pcq dans notre cahier A-> 1, il faut que lon enleve 1 pour que ca 
        # fonctionne avec les nbre ascii
        n = columnNumber -1
        return self.convertToTitle(n // 26) + chr(n % 26 + ord('A'))