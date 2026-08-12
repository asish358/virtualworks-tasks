from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Add current element to the frequency map
            count[nums[right]] += 1
            
            # Shrink window from the left until frequency of nums[right] <= k
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
                
            # Update maximum valid subarray length
            max_len = max(max_len, right - left + 1)
            
        return max_len
