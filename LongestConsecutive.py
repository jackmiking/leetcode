from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            left, right = num, num
            if num + 1 in d and d[num + 1] > num:
                right = d[num + 1]
                del d[num + 1]
            if num - 1 in d and d[num - 1] < num:
                left = d[num - 1]
                del d[num - 1]
            if left == right:
                if left not in d:
                    d[left] = left
            else:
                if left not in d or right > d[left]:
                    d[left] = right

                if right not in d or left < d[right]:
                    d[right] = left
        max = 0
        for key in d:
            v = d[key] - key + 1
            if max < v:
                max = v
        return max


if __name__ == '__main__':
    s = Solution()
    a = [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]
    re = s.longestConsecutive(a)
    print(re)
