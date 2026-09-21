class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            cur = nums[i]
            find = target - cur
            if find in mem.keys():
                if mem[find] < i:
                    return [mem[find], i]
                return [i, mem[find]]
            mem[cur] = i