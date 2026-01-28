class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap data structure
        import heapq
        pq = []
        
        # Add the first K elements in the Min-heap
        for i in range(k):
            heapq.heappush(pq, nums[i])
        
        # Process the rest of the elements 
        for i in range(k, len(nums)):
            # Check if a new larger element is found
            if nums[i] > pq[0]:
                heapq.heappop(pq)  # remove the smallest from the min-heap

                # Add the current element to the min-heap
                heapq.heappush(pq, nums[i])
        
        return pq[0]  # Return the kth largest element 

