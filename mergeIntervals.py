class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mar = []
        intervals.sort(key = lambda x:x[0])
        mar.append(intervals[0])
        for i in range (1, len(intervals)):
            if mar[-1][1] >= intervals[i][0] and mar[-1][1] >= intervals[i][1]:
                mar[-1] = mar[-1]
            elif mar[-1][1] >= intervals[i][0] and mar[-1][1] < intervals[i][1]:
                mar[-1] = [mar[-1][0], intervals[i][1]]
            else:
                mar.append(intervals[i])
        return mar