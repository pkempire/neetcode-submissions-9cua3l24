class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums) #store farthest index we can reach at each i
        dp[0] = nums[0] 
        for i in range(1, len(nums)):
            if i>dp[i-1]:
                return False

            dp[i] = max(dp[i-1], i+nums[i])
           
        return True        

