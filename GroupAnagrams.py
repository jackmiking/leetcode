import collections
from typing import List
'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/77/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
        # items={}
        # for s in strs:
        #     chm={}
        #     for i in s:
        #         v=chm.get(i)
        #         if v is None:
        #             chm[i]=1
        #         else:
        #             chm[i]=chm[i]+1
        #     kk=''
        #     keys=sorted (chm)
        #     for key in keys:
        #         kk=kk+key+str(chm[key])
        #     li=items.get(kk)
        #     if li is None:
        #         li=[s]
        #         items[kk]=li
        #     else:
        #         li.append(s)
        # return items.values()
if __name__ == '__main__':
    inp=["eat", "tea", "tan", "ate", "nat", "bat"]
    s=Solution()
    re=s.groupAnagrams(inp)
    print(re)