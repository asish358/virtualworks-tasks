class Solution:

  def maximumLengthSubstring(self, s: str) -> int:
    count = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
      # Add current character to frequency map
      count[s[right]] = count.get(s[right], 0) + 1

      # Shrink window from the left if any character occurs more than twice
      while count[s[right]] > 2:
        count[s[left]] -= 1
        left += 1

      # Update maximum valid window size
      max_len = max(max_len, right - left + 1)

    return max_len
