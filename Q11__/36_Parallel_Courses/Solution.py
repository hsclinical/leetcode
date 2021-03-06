from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        prerequisites = {}
        for relation in relations:
            if relation[1] not in prerequisites:
                prerequisites[ relation[1] ] = []
            prerequisites[ relation[1] ].append( relation[0] )

        maxDepth = 0
        visited = {}
        for i in range(1, n+1):
            if i in visited:
                continue
            else:
                if i not in prerequisites:
                    curDepth = 1
                    visited[ i ] = 1
                    if curDepth > maxDepth:
                        maxDepth = curDepth
                else:
                    curDepth = self.dfs(prerequisites, visited, i, [])
                    if curDepth == -1:
                        maxDepth = -1
                        break
                    else:
                        if curDepth > maxDepth:
                            maxDepth = curDepth
        return maxDepth


    def dfs(self, prerequisites, visited, curNode, curPath):
        if curNode in curPath:
            return -1

        if curNode not in prerequisites:
            visited[ curNode ] = 1
            return 1
        else:
            maxDepth = 1
            for prevNode in prerequisites[ curNode ]:
                if prevNode in visited:
                    if visited[ prevNode ] > maxDepth:
                        maxDepth = visited[ prevNode ]
                else:
                    curDepth = self.dfs(prerequisites, visited, prevNode, [ curNode ] + curPath[:])
                    if curDepth == -1:
                        return -1
                    else:
                        visited[ prevNode ] = curDepth
                        if visited[ prevNode ] > maxDepth:
                            maxDepth = visited[ prevNode ]
            return maxDepth + 1
