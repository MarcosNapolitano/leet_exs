class Solution:
    def diagonalSum(self, matrix):
        first = matrix[0][0]+matrix[0][len(matrix[0])-1]
        last = matrix[len(matrix)-1][0]+matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]
        if len(matrix)%2 == 0:
        
            return first + last

        else:
            middle = matrix[len(matrix)//2][len(matrix[len(matrix)//2])//2]
            return first + last + middle



mat =        [[1,2,3],
              [4,5,6],
              [7,8,9]]

solucion = Solution()

print(solucion.diagonalSum(mat))