# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.q
# 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        path_sums = [triangle[0]]

        last_index = 0
        
        for i in range(1, len(triangle)):
            path_sums.append([])
            path_sums[i].append(triangle[i][0] + path_sums[i-1][0])
            for j in range(1, len(triangle[i])-1):
                path_sums[i].append(triangle[i][j] + min(path_sums[i-1][j-1], path_sums[i-1][j]))
            path_sums[i].append(triangle[i][i] + path_sums[i-1][i-1])
                
        return min(path_sums[len(path_sums)-1])
