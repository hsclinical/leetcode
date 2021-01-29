from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentToPath = {}
        for singleString in paths:
            cells = singleString.split()
            if len(cells) > 1:
                for i, cell in enumerate(cells):
                    if i == 0:
                        curPath = cells[0]
                    else:
                        bgnIdx = cell.find('(')
                        fileName = cell[:bgnIdx]
                        fileContent = cell[(bgnIdx+1):-1]
                        fullPath = curPath + '/' + fileName
                        if fileContent in contentToPath:
                            contentToPath[ fileContent ].append(fullPath)
                        else:
                            contentToPath[ fileContent ] = [ fullPath ]

        outList = []
        for content in contentToPath:
            if len( contentToPath[content] ) >= 2:
                outList.append( contentToPath[content] )
        return( outList )