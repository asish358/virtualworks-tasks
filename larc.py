class SegmentTree:

    def __init__(self, s: str):
        self.n = len(s)
        self.chars = list(s)
        # Tree stores tuples: (max_len, pref_len, suff_len, left_char, right_char)
        self.tree = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _merge(self, left, right, left_len, right_len):
        l_max, l_pref, l_suff, l_left, l_right = left
        r_max, r_pref, r_suff, r_left, r_right = right

        res_left = l_left
        res_right = r_right

        # Calculate prefix length
        res_pref = l_pref
        if l_pref == left_len and l_right == r_left:
            res_pref += r_pref

        # Calculate suffix length
        res_suff = r_suff
        if r_suff == right_len and l_right == r_left:
            res_suff += l_suff

        # Calculate max repeating substring length
        res_max = max(l_max, r_max)
        if l_right == r_left:
            res_max = max(res_max, l_suff + r_pref)

        return (res_max, res_pref, res_suff, res_left, res_right)

    def _build(self, node, start, end):
        if start == end:
            c = self.chars[start]
            self.tree[node] = (1, 1, 1, c, c)
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)

        self.tree[node] = self._merge(
            self.tree[2 * node],
            self.tree[2 * node + 1],
            mid - start + 1,
            end - mid,
        )

    def update(self, node, start, end, idx, c):
        if start == end:
            self.chars[idx] = c
            self.tree[node] = (1, 1, 1, c, c)
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, c)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, c)

        self.tree[node] = self._merge(
            self.tree[2 * node],
            self.tree[2 * node + 1],
            mid - start + 1,
            end - mid,
        )

    def get_max_length(self):
        return self.tree[1][0]


class Solution:

    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        tree = SegmentTree(s)
        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, tree.n - 1, idx, char)
            ans.append(tree.get_max_length())

        return ans
