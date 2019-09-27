from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        f = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return f


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 8]
    s = Solution()
    r = s.findDuplicate(a)
    print(r)
