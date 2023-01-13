# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        usedInd = []
        retVal = []
        ascending = True
        ascDescCounter = 0
        row = 0
        col = 0
        retVal.append(matrix[row][col])
        usedInd.append((row, col))

        while len(usedInd) < m * n:
            if ascending and ascDescCounter == 0:
                for col in range(col + 1, n):
                    if (row, col) not in usedInd:
                        retVal.append(matrix[row][col])
                        usedInd.append((row, col))
                    else:
                        col -= 1
                        break
                ascDescCounter += 1
            elif ascending and ascDescCounter == 1:
                for row in range(row + 1, m):
                    if (row, col) not in usedInd:
                        retVal.append(matrix[row][col])
                        usedInd.append((row, col))
                    else:
                        row -= 1
                        break
                ascDescCounter = 0
                ascending = False
            elif not ascending and ascDescCounter == 0:
                for col in range(col - 1, -1, -1):
                    if (row, col) not in usedInd:
                        retVal.append(matrix[row][col])
                        usedInd.append((row, col))
                    else:
                        col += 1
                        break
                ascDescCounter += 1
            elif not ascending and ascDescCounter == 1:
                for row in range(row - 1, -1, -1):
                    if (row, col) not in usedInd:
                        retVal.append(matrix[row][col])
                        usedInd.append((row, col))
                    else:
                        row += 1
                        break
                ascDescCounter = 0
                ascending = True
        
        return retVal