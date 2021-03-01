from typing import List
import functools

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        teamLen = len(votes[0])
        rankDict = {}
        for team in votes[0]:
            rankDict[ team ] = [ 0 ] * teamLen

        for vote in votes:
            for i, team in enumerate(vote):
                rankDict[ team ][ i ] += 1

        def compare(item1, item2):
            teamLen = len(item1[0])
            for i in range(teamLen):
                if item1[0][i] < item2[0][i]:
                    return 1
                elif item1[0][i] > item2[0][i]:
                    return -1

            if item1[1] > item2[1]:
                return 1
            elif item1[1] < item2[1]:
                return -1
            else:
                return 0

        rankList = [ ( rankDict[x], x) for x in rankDict ]
        rankList.sort( key=functools.cmp_to_key(compare) )

        teamList = [ x[1] for x in rankList ]

        return ''.join(teamList)

