class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pDist = [ (x[0]**2 + x[1]**2, x) for x in points ]
        pDist.sort()
        outList = [ x[1] for x in pDist[:K] ]
        return outList