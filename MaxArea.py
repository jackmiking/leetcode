from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        left=0
        right=height.__len__()-1
        while right>left:
            h=min(height[left],height[right])
            area=h*(right-left)
            if max<area:
                max=area
            if height[left]<height[right]:
                left+=1
            elif height[left]==height[right]:
                left+=1
                right-=1
            else:
                right=right-1
        return max
if __name__ == '__main__':
    a=[1,8,6,2,5,4,8,3,7]
    s=Solution()
    print(s.maxArea(a))
