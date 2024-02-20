# Gas station
# O(n) time | O(1) space
# I don't know why this works, but it works =))
# This is a solution from LeetCode ;((
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curGas = 0
        start = 0
        for i in range(len(gas)):
            curGas += gas[i] - cost[i]
            if curGas < 0:
                start = i+1
                curGas = 0
        return start