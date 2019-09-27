from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/55/array-and-strings/127/
        """
        row = board.__len__()
        if row == 0:
            return
        col = board[0].__len__()
        for i in range(row):
            for j in range(col):
                v = self.getValueOfAround(board, row, col, i, j)
                alive = 0
                if (v == 2 and board[i][j] == 1) or v == 3:
                    alive = 1
                alive = (alive << 1) + board[i][j]
                board[i][j] = alive
        for i in range(row):
            for j in range(col):
                board[i][j] = board[i][j] >> 1

    def getValueOfAround(self, board, row, col, i, j):
        pa, pb = (i - 1 if i - 1 > 0 else 0, j - 1 if j - 1 > 0 else 0), (
            i + 1 if i + 1 < row else row - 1, j + 1 if j + 1 < col else col - 1)
        v = -board[i][j]
        for bi in range(pb[0] - pa[0] + 1):
            for bj in range(pb[1] - pa[1] + 1):
                v = v + (board[pa[0] + bi][pa[1] + bj] & 1)
        return v


if __name__ == '__main__':
    a = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s = Solution()
    s.gameOfLife(a)
    print(a)
