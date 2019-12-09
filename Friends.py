from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        find_list = [-1] * n
        for i in range(n):
            for j in range(i):
                if i == j or M[i][j]==0:
                    continue;
                else:
                    ti=self.getTop(find_list,i)
                    tj=self.getTop(find_list,j)
                    if ti!=tj:
                        find_list[tj]=ti
        return len([x for x in find_list if x == -1])
    def getTop(self,find_list,i):
        while find_list[i]!=-1:
            i=find_list[i]
        return i
if __name__ == '__main__':
    inp=[[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
    inp2=[[1,1,0],
 [1,1,0],
 [0,0,1]]
    inp3=[[1,1,1],[1,1,1],[1,1,1]]
    s=Solution()
    l=s.findCircleNum(inp3)
    print(l)