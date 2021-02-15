from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        inToOut = {}

        for ticket in tickets:
            if ticket[0] not in inToOut:
                inToOut[ ticket[0] ] = []
            inToOut[ ticket[0] ].append( ticket[1] )

        for inAirport in inToOut:
            inToOut[inAirport].sort()

        outcome, stopList = self.dfs(inToOut, tickets, "JFK")

        return stopList

    def dfs(self, inToOut, tickets, curAirport):
        if len(tickets) == 0:
            return True, [ curAirport ] 
        elif curAirport in inToOut:
            nextAirportList = inToOut[ curAirport ]
            for nextAirport in nextAirportList:
                if [ curAirport, nextAirport ] in tickets:
                    nextTickets = tickets[:]
                    nextTickets.remove( [ curAirport, nextAirport ] )
                    outcome, stopList = self.dfs(inToOut, nextTickets, nextAirport)
                    if outcome:
                        stopList.insert(0, curAirport)
                        return outcome, stopList
            return False, []
        else:
            return False, []