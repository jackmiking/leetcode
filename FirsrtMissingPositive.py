import math
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=nums.__len__()
        item=-1
        res=l+1
        for i in range(l):
            if nums[i]>0 and nums[i]<=l:
                item=nums[i]

            nums[i]=-1
            while item>0:
                tem=nums[item-1]
                if tem==item:
                    item=-1
                else:
                    nums[item-1]=item
                    item=tem
        for i in range(l):
            if nums[i]>0:
                continue
            res=i+1
            break

        return res
if __name__ == '__main__':
        n=[9,8,7,6,5,4,3,2,1]
        s=Solution()
        r=s.firstMissingPositive(n)
        print(r)