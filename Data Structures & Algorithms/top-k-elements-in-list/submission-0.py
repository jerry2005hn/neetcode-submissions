class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        for num in nums:
            if num not in track:
                track[num] = 1
            else:
                track[num] += 1
        freq = [[] for i in range(len(nums)+1)]
        for num, numCount in track.items():
            freq[numCount].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                