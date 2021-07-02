class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        outList = []
        evenSum = sum( [ x for x in nums if x%2 == 0 ] )
        for query in queries:
            prevNum = nums[ query[1] ]
            nums[ query[1] ] += query[0]
            curNum = nums[ query[1] ]
            if prevNum % 2 == 0 and curNum % 2 == 0:
                evenSum = evenSum - prevNum + curNum
            elif prevNum % 2 != 0 and curNum % 2 == 0:
                evenSum = evenSum + curNum
            elif prevNum % 2 == 0 and curNum % 2 != 0:
                evenSum = evenSum - prevNum
            else:
                pass

            outList.append(evenSum)
        return outList