# Minimum Time to Make Rope Colorful
# O(n) time | O(1) space
# colors = "abaac"
# neededTime = [1,2,3,4,5]
# remove all balloons except the balloon with max time when the color is the same
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0
        while i < len(colors):
            max_time = 0
            cur_time = 0
            j = i
            while j < len(colors):
                if colors[i] != colors[j]:
                    break
                cur_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
                j += 1
            tmp = cur_time - max_time
            res += tmp
            i = j
        
        return res