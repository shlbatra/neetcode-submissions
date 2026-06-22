class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1 o(nlogn)
        # input and go through each 
        # mantain dictionary with frequency -> retirn k most frequent sorted dictionary
        # O(n) space and time complexity
        # Approach 2 (not required) - extra than approach 1
        # Sliding window (Assumption sorted)
        # keep iterating right pointer till change compare to k
        # if changed, update l to where right + 1
        # Use max heap with key as number of occurances and pop k times 
        # Initialize heap using heapify - O(n), pop k times, klog(n)
        # Even better soln - O(n) space and memory using bucket sort
        # [1, 1, 1, 2, 2, 100] - values unbounded so input array unbounded
        # i.        0, 1, 2, ......, 100
        # count.      , 3, 2,      , 1
        # instead 
        # count.    0, 1, 2, 3, 4, 5, 6 -> Index max len of input array, space O(n+1)
        # values.   [], [100], [2], [1], [], [], []
        # Then look for values from 6 to down until get top k 
        # Time complexity O(nlogk), O(n)
        from collections import defaultdict
        import heapq
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        # {1: 3, 2: 2, 100: 1}
        # Use Min Heap - always keep smallest element at top.
        heap, ans = [], []
        print(freq_dict)
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap) # Smallest ones are popped once k is reached
        print(heap)
        while k > 0:
            element = heapq.heappop(heap)[1]
            ans.append(element)
            k = k - 1
        return ans 
        


