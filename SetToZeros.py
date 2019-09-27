'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/76/
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = matrix.__len__()
        if row < 1:
            return
        col = 0
        col = matrix[0].__len__()

        firstIsZero = False
        firstRowIsZero = False
        firstColIsZero = False
        if matrix[0][0] == 0:
            firstIsZero = True
        for i in range(1,row):
            if matrix[i][0] == 0:
                firstColIsZero = True
                matrix[i][0]=0

        for j in range(1,col):
            if matrix[0][j] == 0:
                firstRowIsZero = True
                matrix[0][j]=0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0
        for j in range(1, col):
            if matrix[0][j] ==0:
                for i in range(row):
                    matrix[i][j] = 0
        if firstIsZero or firstColIsZero:
            for i in range(row):
                matrix[i][0] = 0
        if firstIsZero or firstRowIsZero:
            for j in range(col):
                matrix[0][j] = 0



if __name__ == '__main__':
    s = Solution()
    m = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    s.setZeroes(m)
    print(m)
    m=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    s.setZeroes(m)
    print(m)