class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix[0])-1

        while l < r:
            # on dois faie r-l car cest r-l iterations
            # que lon doit faire pour changer la position de chaque
            for i in range(r-l):
                # For 1 iteration of i
                # bottom-left  → top-left
                # bottom-right → bottom-left
                # top-right    → bottom-right
                # top-left     → top-right
                top =  l
                bottom = r

                temp = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]

                matrix[bottom-i][l] = matrix[bottom][r -i]

                matrix[bottom][r -i] = matrix[top +i][r]

                matrix[top +i][r] = temp
            r -= 1
            l +=1
