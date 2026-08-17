from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        leftBest = [[0] * n for _ in range(n)]
        rightBest = [[0] * n for _ in range(n)]
        
        leftPtr = [i - 1 for i in range(n)]
        rightPtr = [i for i in range(n)]
        
        for i in range(n):
            leftBest[i][i] = stoneValue[i]
            rightBest[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total = prefix[r + 1] - prefix[l]
                
                while leftPtr[l] + 1 <= r - 1:
                    k = leftPtr[l] + 1
                    leftSum = prefix[k + 1] - prefix[l]
                    if 2 * leftSum > total:
                        break
                    leftPtr[l] += 1
                    
                while rightPtr[l] <= r - 1:
                    k = rightPtr[l]
                    leftSum = prefix[k + 1] - prefix[l]
                    if 2 * leftSum >= total:
                        break
                    rightPtr[l] += 1
                    
                best = 0
                if leftPtr[l] >= l:
                    best = leftBest[l][leftPtr[l]]
                    
                if rightPtr[l] <= r - 1:
                    best = max(best, rightBest[rightPtr[l] + 1][r])
                    
                dp[l][r] = best
                leftBest[l][r] = max(leftBest[l][r - 1], dp[l][r] + total)
                rightBest[l][r] = max(rightBest[l + 1][r], dp[l][r] + total)
                
        return dp[0][n - 1]
