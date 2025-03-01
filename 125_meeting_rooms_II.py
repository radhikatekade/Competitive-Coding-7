# Time complexity - O(nlogn) # because of sorting
# Space complexity - O(n) # because of heap

# Approach - Maintain a heap for all the meeting ending time, everytime the start of the next meeting is
# greater than or equal to the top element of heap, pop the element, perform the heapify. In the end, return
# the length of the heap.

from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) == 0:
            return 0
        
        intervals = sorted(intervals)
        meetingRooms = [] # maintaing heap
        heapq.heappush(meetingRooms, intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= meetingRooms[0]:
                heapq.heappop(meetingRooms)
            heapq.heappush(meetingRooms, intervals[i][1])
            print(meetingRooms)
        return len(meetingRooms)