#!/usr/bin/python

from Solution import Solution

'''
obj = MyCalendarTwo()
print(obj.book(10,20))
print(obj.book(50,60))
print(obj.book(10,40))
print(obj.book(5,15))
print(obj.book(5,10))
print(obj.book(25,55))
'''
obj = Solution()

#inputA = [["a","b"],["b","c"]]
#inputB = [2.0,3.0]
#inputC = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

#inputA = [["a","b"],["b","c"],["bc","cd"]]
#inputB = [1.5,2.5,5.0]
#inputC = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

#inputA = [["a","b"],["c","d"],["e","f"],["a","c"],["c","f"]]
#inputB = [2.0,3.0,4.0,5.0,6.0]
#inputC = [["c","e"]]

inputA = [["a","b"]]
inputB = [0.5]
inputC = [["a","b"],["b","a"],["a","c"],["x","y"]]

out = obj.calcEquation(equations=inputA, values=inputB, queries=inputC)
print(out)
