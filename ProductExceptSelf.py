from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(nums.__len__()):
            if i > 0:
                res.append( res[i - 1] * nums[i - 1])
            else:
                res.append(1)
        i = nums.__len__() - 1
        right = 1
        while i > -1:
            if i == nums.__len__() - 1:
                res[i] = res[i] * right
            else:
                right = right * nums[i + 1]
                res[i] = res[i] * right
            i = i - 1
        return res
