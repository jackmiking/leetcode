from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowsMax = list()
        result = []
        for i in range(nums.__len__()):
            num = nums[i]
            while windowsMax.__len__() != 0 and nums[windowsMax[-1]] < num:
                windowsMax.pop()
            windowsMax.append(i)
            if i >= k - 1:

                if windowsMax[0] + k == i:
                    windowsMax.pop(0)
                result.append(nums[windowsMax[0]])
        return result


if __name__ == '__main__':
    inputs =[1,3,1,2,0,5]
    s = Solution()
    r = s.maxSlidingWindow(inputs, 3)
    print(r)
