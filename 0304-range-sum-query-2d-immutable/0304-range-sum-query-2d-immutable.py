class NumMatrix(object):

    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat =[[0]*(cols + 1) for r in range(rows +1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r+1][c+1] =prefix + above
                
            
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, r1, c1, r2, c2):
        r1 ,c1 ,r2, c2  = r1 +1 , c1 +1, r2+ 1, c2+ 1
        bottomright = self.sumMat[r2][c2]
        topright = self.sumMat[r1 -1][c2]
        bottomleft =  self.sumMat[r2][c1 - 1]
        topleft = self.sumMat[r1 -1][c1 - 1]
        return  bottomright - topright - bottomleft + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)