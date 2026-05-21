class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsSeen = set()
        colSeen = set()

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowsSeen.add(r)
                    colSeen.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in rowsSeen or c in colSeen:
                    matrix[r][c] = 0