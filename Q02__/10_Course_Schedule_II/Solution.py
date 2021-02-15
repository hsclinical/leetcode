from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))
        else:
            prevCourse = {}
            for prerequisite in prerequisites:
                if prerequisite[0] not in prevCourse:
                    prevCourse[ prerequisite[0] ] = []
                prevCourse[ prerequisite[0] ].append( prerequisite[1] )

            stack = []
            visited = set()
            for i in range(numCourses):
                outcome = self.addCourse(prevCourse, stack, visited, [i], i)
                if not outcome:
                    return []
            return stack

    def addCourse(self, prevCourse, stack, visited, coursePath, course):
        if course not in visited:
            if course not in prevCourse:
                stack.append( course )
                visited.add( course )
            else:
                prevList = prevCourse[ course ]
                for prevC in prevList:
                    if prevC in coursePath:
                        return False
                    else:
                        newPath = coursePath[:] + [ prevC ]
                        outcome = self.addCourse(prevCourse, stack, visited, newPath, prevC)
                        if not outcome:
                            return False
                stack.append( course )
                visited.add( course )
        return True