class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # position, from, to
        changes = list(zip(indexes, sources, targets))
        changes.sort(key=lambda x: x[0], reverse=True)
        for change in changes:
            if S[change[0]:change[0]+len(change[1])] == change[1]:
                S = S[:change[0]] + change[2] + S[(change[0]+len(change[1])):]
        return S
