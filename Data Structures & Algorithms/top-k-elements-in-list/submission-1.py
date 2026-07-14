class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # integer : count 
        integer_count = {}

        for int in nums: 
            if int not in integer_count: 
                integer_count[int] = 0 
            integer_count[int] += 1  

        sorted_integer_count = sorted(tuple(integer_count.items()), key = lambda x:x[1], reverse =  True)

        output = [] 

        for i in range(k): 
            output.append(sorted_integer_count[i][0])

        return output


        