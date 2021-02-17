from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        peopleLen = len(people)
        if peopleLen == 1:
            return people
        else:
            sortedPeople = sorted(people, key=lambda x: (x[0],x[1]))
            outcome = [ 0 ] * peopleLen
            for person in sortedPeople:
                idx = 0
                for i, num in enumerate(outcome):
                    if num == 0:
                        if idx == person[1]:
                            outcome[i] = person
                            break
                        else:
                            idx += 1
                    else:
                        if num[0] == person[0]:
                            idx += 1
            return outcome