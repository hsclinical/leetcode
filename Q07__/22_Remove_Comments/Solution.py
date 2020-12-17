from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        outList = []
        inCommentBlock = False
        for line in source:
            if inCommentBlock:
                blockEndCommentIndex = line.find("*/")
                if blockEndCommentIndex == -1:
                    # the whole line has been commented out
                    continue
                else:
                    inCommentBlock = False
                    line = self.lineRemoveLeft(line, blockEndCommentIndex)
                    if line == "":
                        continue
                    else:
                        previousLine = outList.pop()
                        line = previousLine + line

            line = self.simplifyLine(line)
            lineCommentIndex = line.find("//")
            blockBgnCommentIndex = line.find("/*")
            if blockBgnCommentIndex == -1 and lineCommentIndex == -1:
                # no comment
                if line != "":
                    outList.append(line)
            elif blockBgnCommentIndex == -1 or (blockBgnCommentIndex != -1 and lineCommentIndex != -1 and blockBgnCommentIndex > lineCommentIndex):
                # line comment only or line comment show up first
                line = self.lineRemoveRight(line, lineCommentIndex)
                if line != "":
                    outList.append(line)
            elif lineCommentIndex == -1 or (blockBgnCommentIndex != -1 and lineCommentIndex != -1 and blockBgnCommentIndex < lineCommentIndex):
                # block comment only or block comment show up first
                blockEndCommentIndex = line.find("*/", blockBgnCommentIndex+2)
                if blockEndCommentIndex == -1:
                    inCommentBlock = True
                    line = self.lineRemoveRight(line, blockBgnCommentIndex)
                    if line != "":
                        outList.append(line)
                else:
                    # should not happen, complicated case has been simplified at simplifyLine step
                    pass
            else:
                # blockBgnCommentIndex == lineCommentIndex which is impossible
                pass
        return outList

    def simplifyLine(self, line):
        newLine = line
        while True:
            lineCommentIndex = newLine.find("//")
            blockBgnCommentIndex = newLine.find("/*")
            if blockBgnCommentIndex != -1 and (lineCommentIndex == -1 or (lineCommentIndex != -1 and lineCommentIndex > blockBgnCommentIndex)):
                blockEndCommentIndex = newLine.find("*/", blockBgnCommentIndex+2)
                if blockEndCommentIndex == -1:
                    break
                else:
                    newLine = self.lineRemoveBetween(newLine, blockBgnCommentIndex, blockEndCommentIndex)
            else:
                break
        return newLine

    def lineRemoveLeft(self, line, index):
        if index + 2 >= len(line):
            return ""
        else:
            newLine = line[index + 2:]
            return newLine

    def lineRemoveRight(self, line, index):
        if index == 0:
            return ""
        else:
            newLine = line[:index]
            return newLine

    def lineRemoveBetween(self, line, indexBgn, indexEnd):
        newLine = ""
        if indexBgn != 0:
            newLine = line[:indexBgn]
        if indexEnd + 2 != len(line):
            newLine += line[indexEnd + 2:]
        return newLine