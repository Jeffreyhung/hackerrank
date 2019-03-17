# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x.start)
        rooms = []
        rooms.append(intervals[0].end)
        for i in intervals[1:]:
            if rooms[0] <= i.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
                
        return len(rooms)
        