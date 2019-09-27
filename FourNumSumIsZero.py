'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/55/array-and-strings/125/
'''
import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_count = collections.Counter(a + b for a in A for b in B)
        return sum(sum_count[-c - d] for c in C for d in D)
