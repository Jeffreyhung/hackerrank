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
        inter_list=[]
        ans = []
        for i in intervals:
            inter_list.append([i.start, i.end])
        while inter_list:
            if len(inter_list) == 1:
                ans.append(inter_list[0])
                break
            else:
                if (inter_list[0][1] >= inter_list[1][0]) and (inter_list[0][1] <= inter_list[1][1]):
                    inter_list[0][1] = inter_list[1][1]
                    del inter_list[1]
                elif (inter_list[0][1] >= inter_list[1][0]) and (inter_list[0][1] > inter_list[1][1]):
                    del inter_list[1]
                else:
                    ans.append(inter_list[0])
                    del inter_list[0]
        return ans