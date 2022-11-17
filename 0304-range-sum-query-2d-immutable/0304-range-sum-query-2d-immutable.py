class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type self.matrix: List[List[int]]
        """
        self.matrix = matrix
        for row in range(len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                self.matrix[row][col] += self.matrix[row][col - 1]
        for row in range(1, len(self.matrix)):
            for col in range(len(self.matrix[0])):
                self.matrix[row][col] += self.matrix[row - 1][col]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        gebdaw = self.matrix[row2][col2]
        leftMikenes = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        topMikenes = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        metdemerewa = self.matrix[row1 - 1][col1 - 1] if (col1 > 0 and row1 > 0) else 0
        
        return gebdaw - leftMikenes - topMikenes + metdemerewa
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(self.matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)