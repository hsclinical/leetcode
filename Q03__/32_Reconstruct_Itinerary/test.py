#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
A = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
out = obj.findItinerary(A)
print(out)
