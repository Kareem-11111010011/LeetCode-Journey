class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [0] * len(grid[0])
        prefix[0] = grid[1][0]
        for j in range(1, len(grid[0])):
            prefix[j] = prefix[j - 1] + grid[1][j]

        postfix = [0] * len(grid[0])
        postfix[-1] = grid[0][-1]
        for j in range(len(grid[0]) - 2, -1, -1):
            postfix[j] = postfix[j + 1] + grid[0][j]

        minMax = float('inf')
        for j in range(len(grid[0])):
            if j == 0:
                if j + 1 < len(postfix):
                    lsf = postfix[j + 1]
                else:
                    lsf = 0
            elif j == len(grid[0]) - 1:
                lsf = prefix[j - 1]
            else:
                lsf = max(prefix[j - 1], postfix[j + 1])

            if lsf < minMax:
                minMax = lsf

        return minMax
