class Solution:
    def solve(self, items):
        row, col = items.__len__(), items[0].__len__()
        max_map, rev_map, max = self.getCharMap(items)
        res = []
        step = 1
        mul = 2
        while step >= 1:
            left_num, result, tem_map, tem_rev_map = self.merge(max_map, rev_map, row, col, step)

            if result.__len__() > 1:
                res = result
                max += step
                max_map = tem_map
                rev_map = tem_rev_map

            else:
                mul = 0.5
            step = int(step * mul)
        return max, res

    def merge(self, status_map, rev_map, inRow, inCol, step):
        new_map = {}
        new_rev_map = {}
        left_num = 0
        result = []
        for hashValue in status_map:
            if status_map[hashValue].__len__() < 2:
                continue
            for row_col in status_map[hashValue]:
                row, col = row_col
                s = ""
                if col + step > inCol or row + step > inRow:
                    continue
                left = rev_map.get((row + step, col))
                top = rev_map.get((row, col + step))
                corner = rev_map.get((row + step, col + step))
                if left is None or top is None or corner is None:
                    continue
                v = hash(left + top + corner)
                lists = new_map.get(v)
                if lists is None:
                    lists = []
                    new_map[v] = lists
                new_rev_map[(row, col)] = v
                left_num += 1
                lists.append((row, col))
                if lists.__len__() > 1:
                    result = lists
        return left_num, result, new_map, new_rev_map

    def getCharMap(self, items):
        item_map = {}
        max_len = 0
        row, col = items.__len__(), items[0].__len__()
        rev_map = {}
        for i in range(row):
            for j in range(col):
                lists = item_map.get(items[i][j])
                if lists is None:
                    lists = []
                    item_map[items[i][j]] = lists
                lists.append((i, j))
                max_len = max(lists.__len__() , max_len)
                rev_map[(i, j)] = items[i][j]
        return item_map, rev_map, 1 if max_len > 1 else 0


if __name__ == '__main__':
    row_col = input()
    while row_col == "":
        row_col = input()
    row, col = row_col.split(" ")
    items = []
    for i in range(int(row)):
        s = input()
        items.append(s)
    s = Solution()
    max, res = s.solve(items)
    print(max)
    if max > 0:
        for i in range(2):
            print(res[i][0] + 1, res[i][1] + 1)
        '''
5 10
mklghiegbta
jtegkltjzfb
qhmkljkmhqc
fzjtebgetjd
moqhmlglkme

        '''
