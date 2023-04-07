class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mar = []
        m =[]
        for i in range (len(points)):
            m.append([i, sqrt(pow(0 - points[i][0], 2) + pow(0 - points[i][1], 2))])
        m.sort(key=lambda m:m[1])
        for i in range (k):
            mar.append(points[m[i][0]])
        return mar