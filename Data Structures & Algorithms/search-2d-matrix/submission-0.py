class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_count = len(matrix)
        col_count = len(matrix[0])
        output = False

        low = 0
        high = row_count * col_count - 1

        while (low <= high):
            mid = low + (high - low // 2)
            value = matrix[mid // col_count][mid % col_count]

            if value == target:
                return True
            if value < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
            
