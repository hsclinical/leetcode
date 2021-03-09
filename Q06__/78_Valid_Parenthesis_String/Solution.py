class Solution:
    def checkValidString(self, s: str) -> bool:
        while True:
            origLen = len(s)
            s = s.replace('()', '')
            newLen = len(s)
            if origLen == newLen:
                break

        score = [0]
        for char in s:
            if char == '(':
                score = [ i+1 for i in score ]
            elif char == ')':
                score = [ i-1 for i in score if i-1 >= 0 ]
                if len(score) == 0:
                    return False
            else:
                score += [ score[-1] + 1 ]
                if score[0] != 0:
                    score = [ score[0] - 1 ] + score

        if 0 in score:
            return True
        else:
            return False
