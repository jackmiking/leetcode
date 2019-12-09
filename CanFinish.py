'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/57/trees-and-graphs/142/
'''
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps=[[0 for i in range(numCourses)] for j in range(numCourses)]
        lists=[0]*numCourses
        for i in range(len(prerequisites)):
            item=prerequisites[i]
            maps[item[1]][item[0]]=1
            lists[item[0]]+=1
        qu=[i for i in range(len(lists)) if lists[i]==0]
        while len(qu)>0:
            item=qu.pop()
            for i in range(numCourses):
                if maps[item][i]==1:
                    lists[i]-=1
                    if lists[i]==0:
                        qu.append(i)
        lena=len([x for x in lists if x>0])
        if lena>0:
            return False
        else:
            return True
if __name__ == '__main__':
    s=Solution()
    n,li=3,[[1,0],[1,2],[0,1]]
    r=s.canFinish(n,li)
    print(r)
    a=set()
    a.pop()


