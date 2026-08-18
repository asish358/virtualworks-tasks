from collections import defaultdict
from typing import List


class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = defaultdict(int)

        # Count in how many size-k subarrays each unique number appears
        for i in range(n - k + 1):
            seen_in_window = set(nums[i : i + k])
            for num in seen_in_window:
                subarray_count[num] += 1

        # Find the maximum element with a count of exactly 1
        valid_nums = [
            num for num, count in subarray_count.items() if count == 1
        ]
        return max(valid_nums) if valid_nums else -1
