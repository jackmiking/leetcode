from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix.__len__()==0:
            return []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        border = [0,matrix[0].__len__()-1, matrix.__len__()-1,  0]
        i, j, d = 0,0,0
        res = []
        while True:
            res.append(matrix[i][j])
            toi = i + direction[d][0]
            toj = j + direction[d][1]
            if toi >= border[0] and toi <= border[2] and toj >= border[3] and toj <= border[1]:
                i = toi
                j = toj
                continue
            else:
                if d > 0 and d < 3:
                    border[d] = border[d] - 1
                else:
                    border[d] = border[d] + 1

                d = (d + 1) % 4
                toi = i + direction[d][0]
                toj = j + direction[d][1]
                if toi >= border[0] and toi <= border[2] and toj >= border[3] and toj <= border[1]:
                    i = toi
                    j = toj
                    continue
                else:
                    break
        return res


if __name__ == '__main__':
    inp = [
        [1]
    ]
    s=Solution()
    re=s.spiralOrder(inp)
    print(re)
