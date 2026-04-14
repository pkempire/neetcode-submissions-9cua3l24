class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni,ne = newInterval
        n = len(intervals)
        i=0
        res = []
        while i<n and intervals[i][1] < ni:
            res.append(intervals[i])
            i+=1
        while i<n and intervals[i][0] <= ne:
            ni = min(ni, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i+=1 
        res.append([ni,ne])   
        while i<n:
            res.append(intervals[i])
            i+=1
        return res