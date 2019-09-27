from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a ,b=None,None
        for i in range(nums.__len__()-1):
            if nums[i]<nums[i+1]:
                if a is None:
                    a=nums[i]
                    b=nums[i+1]
                elif a<nums[i] or b <nums[i+1]:
                    return True
                else:
                    a=nums[i]
                    b=nums[i+1]
            i=i+1

        return False
if __name__ == '__main__':
    s=Solution()
    print(s.increasingTriplet([7,3,6,2,4,1,5]))