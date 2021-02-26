# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.numList = self.nestedToNormal( nestedList )
        self.numLen = len(self.numList)
        self.numIdx = -1
    
    def next(self) -> int:
        self.numIdx += 1
        return self.numList[ self.numIdx ]
    
    def hasNext(self) -> bool:
         if self.numIdx <= self.numLen-2:
             return True
         else:
             return False

    def nestedToNormal(self, nestedList):
        numList = []
        for singleElem in nestedList:
            if singleElem.isInteger():
                numList.append( singleElem.getInteger() )
            else:
                numList += self.nestedToNormal( singleElem.getList() )
        return numList

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())