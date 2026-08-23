class Solution:

    def sumGame(self, num: str) -> bool:
        n = len(num)
        sum_diff = 0
        q_diff = 0

        for i in range(n):
            sign = 1 if i < n // 2 else -1

            if num[i] == "?":
                q_diff += sign
            else:
                sum_diff += sign * int(num[i])

        # Bob wins if sum_diff + (q_diff / 2) * 9 == 0
        return sum_diff * 2 != -q_diff * 9
