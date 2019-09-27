'''
https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = s.__len__()
        if slen==0:
            return ""
        max_len = (slen + 1) // 2
        center_ind = max_len - 1
        bias = 0
        direction = -1
        max = 0
        maxs = ""
        while slen-2*bias+1 > max:
            ind = center_ind + bias * direction
            left, right = self.sol(s, ind, slen)
            len = right - left + 1
            if max < len:
                max = len
                maxs = s[left:right + 1]
            direction = direction * -1
            if direction > 0:
                bias += 1
        return maxs

    def sol(self, s, center_index, len):
        bias = 1
        while center_index - bias >= 0 and center_index + bias < len:
            if s[center_index - bias] == s[center_index + bias]:
                bias = bias + 1
                continue
            else:
                break
        left, right = center_index - bias + 1, center_index + bias - 1
        if center_index<len-1 and s[center_index] == s[center_index + 1]:
            bias = 1
            while center_index - bias >= 0 and center_index + bias + 1 < len:
                if s[center_index - bias] == s[center_index + bias + 1]:
                    bias = bias + 1
                    continue
                else:
                    break
            l2, r2 = center_index - bias + 1, center_index + bias
            if r2 - l2 > right - left:
                left, right = l2, r2
        return left, right


if __name__ == '__main__':
    s = Solution()
    ss = "banana"
    c = s.longestPalindrome(ss)
    print(c)
