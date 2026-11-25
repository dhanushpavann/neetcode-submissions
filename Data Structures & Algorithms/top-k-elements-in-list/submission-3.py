class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}
        for num in nums:
            occur[num] = 1 + occur.get(num,0)
        
        heap = []
        for key in occur:
            heapq.heappush(heap,(occur[key],key))
            if len(heap) >k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        