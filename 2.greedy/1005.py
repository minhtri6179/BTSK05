# Maximize Sum Of Array After K Negations
# Time: O(n) | Space: O(1)
# [-4,-6,9,-2,2] | 4
# [4,6,9,-2,2] 
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        have_zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                have_zero = True
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            if k == 0:
                break
        min_num = 9999999999
        for i in range(len(nums)):
            min_num = min(min_num, nums[i])
            res += nums[i]
        if have_zero:
            return res
        if (k%2 != 0):
            res -= min_num*2
        return res