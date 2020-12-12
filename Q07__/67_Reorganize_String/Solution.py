class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = {i : S.count(i) for i in set(S)} 
        length = len(S)
        maxCount = (length + 1)//2
        for letter in freq:
            if freq[ letter ] > maxCount:
                return ""

        sortedKeys = sorted(freq, key=freq.get, reverse=True)
        medianS = ""
        for letter in sortedKeys:
            medianS += letter * freq[ letter ]
        part1 = medianS[:maxCount]
        part2 = medianS[maxCount:]
        outList = [char for char in part1]
        for i in range(len(part2)):
            outList.insert(2*i+1, part2[i])

        O = ''.join(outList)
        return O