class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} 
        freq = [[] for i in range(len(nums) + 1)] 
        # freq : values (as a list)

        for n in nums: 
            count[n] = count.get(n, 0) + 1

        for n, c in count.items(): 
            freq[c].append(n) 

        res = []

        for l in range(len(freq) - 1, 0, -1): 
            for m in freq[l]: 
                res.append(m)
            if len(res) == k: 
                return res

        

        