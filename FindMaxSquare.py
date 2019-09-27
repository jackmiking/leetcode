class Solution:
    def solve(self, items):
        row, col = items.__len__(), items[0].__len__()
        charlist = self.getCharList(items)
        maxC = 0
        maxij = []

        status_list = []
        current_list = []
        for i in range(row):
            for j in range(col):
                chr = items[i][j]
                charIndexs = charlist[ord(chr) - 97]
                ind = charIndexs.index((i, j))
                bias_counter_map = {}
                for bias in range(charIndexs.__len__() - ind - 1):
                    loc = charIndexs[ind + bias + 1]
                    biasi, biasj = loc[0] - i, loc[1] - j
                    left_count, top_count, corner_count = 0, 0, 0
                    if j > 0:
                        left_count = current_list[j - 1].get((biasi, biasj))
                        if left_count is None:
                            left_count = 0
                    if i > 0:
                        top_count = status_list[j].get((biasi, biasj))
                        if top_count is None:
                            top_count = 0
                    if i > 0 and j > 0:
                        corner_count = status_list[j - 1].get((biasi, biasj))
                        if corner_count is None:
                            corner_count = 0
                    biasCount = min(left_count, top_count, corner_count) + 1
                    bias_counter_map[(biasi, biasj)] = biasCount

                    if biasCount == maxC:
                        if (i - biasCount + 1, j - biasCount + 1) not in maxij:
                            maxij.append((i - biasCount + 1 + 1, j - biasCount + 1 + 1))
                            maxij.append((i - biasCount + 1 + 1 + biasi, j - biasCount + 1 + 1 + biasj))
                        maxC = biasCount
                    elif biasCount > maxC:
                        maxij = [(i - biasCount + 1 + 1, j - biasCount + 1 + 1)]
                        maxij.append((i - biasCount + 1 + 1 + biasi, j - biasCount + 1 + 1 + biasj))
                        maxC = biasCount
                current_list.append(bias_counter_map)
            status_list = current_list
            current_list = []
        return maxC, maxij

    def getCharList(self, items):
        lists = list()
        for i in range(26):
            lists.append(list())
        row, col = items.__len__(), items[0].__len__()
        for i in range(row):
            for j in range(col):
                ind = ord(items[i][j]) - 97
                lists[ind].append((i, j))
        return lists


if __name__ == '__main__':
    row_col = input()
    while row_col=="":
        row_col=input()
    row, col = row_col.split(" ")
    items = []
    for i in range(int(row)):
        s = input()
        items.append(s)
    s = Solution()
    max, res = s.solve(items)
    print(max)
    for a in res:
        print(a[0], a[1])
        '''
5 10
mklghiegbta
jtegkltjzfb
qhmkljkmhqc
fzjtebgetjd
moqhmlglkme

        '''
