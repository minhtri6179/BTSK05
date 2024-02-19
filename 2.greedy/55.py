# Jump Game
# Time: O(n) | Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        i = 0
        while i <= max_jump and max_jump < len(nums)-1:
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= (len(nums)-1):
                return True
            i += 1
        
        return max_jump >= (len(nums)-1)