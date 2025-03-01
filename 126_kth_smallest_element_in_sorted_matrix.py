# Time complexity - O(X+Klog(X)) where X=min(K,N)
# Space complexity - O(X) # because of heap

# Approach - 

import heapq
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        minHeap = []
        for r in range(min(k, N)):
            # searching row wise for 0th column
            minHeap.append((matrix[r][0], r, 0))
        
        while k: # Until we find k elements
            element, r, c = heapq.heappop(minHeap)
            if c < N - 1: # searching column-wise for the given row
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1
        return element