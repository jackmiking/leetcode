from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re=set()
        for i in range(1,nums.__len__()-1):
            l = 0;
            r = nums.__len__() - 1;
            while r >i and l<i :
                sum=nums[l]+nums[i]+nums[r]
                if sum>0:
                    r-=1
                    while r>i and nums[r]==nums[r-1]:
                        r-=1
                elif sum<0:
                    l+=1
                else:
                    re.add((nums[l],nums[i],nums[r]))
                    r-=1
                    l+=1
        return re

if __name__ == '__main__':
    sol = Solution()
    re = sol.threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(re)
