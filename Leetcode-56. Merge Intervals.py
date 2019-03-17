# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        ans = []
        if len(intervals) == 0:
            return intervals
        ans.append(intervals[0])
        for i in range (1,len(intervals)):
            if(ans[-1].end >= intervals[i].start):
                if (ans[-1].end < intervals[i].end):
                    ans[-1].end = intervals[i].end
            else:
                ans.append(intervals[i])
        return ans
    
    