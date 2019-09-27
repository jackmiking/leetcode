'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/78/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        len=s.__len__()
        if len<1:
            return 0
        max=1
        cs=set()
        while end <s.__len__():
            while cs.__contains__(s[end]):
               cs.remove(s[start])
               start+=1
            cm=end-start+1
            cs.add(s[end])
            if max<cm:
                max=cm
            end+=1
        return max
if __name__ == '__main__':
    s="pwwkew"
    ss=Solution()
    i=ss.lengthOfLongestSubstring(s)
    print(i)