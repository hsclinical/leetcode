class Solution:
    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        outcome = ''
        numT = num // 1000
        if numT != 0:
            outcome += 'M' * numT
        num = num % 1000

        numT = num // 100
        if numT == 9:
            outcome += 'CM'
        elif numT >= 5 and numT < 9:
            outcome += 'D' + 'C' * (numT - 5)
        elif numT == 4:
            outcome += 'CD'
        elif numT > 0 and numT < 4:
            outcome += 'C' * numT
        else:
            pass
        num = num % 100

        numT = num // 10
        if numT == 9:
            outcome += 'XC'
        elif numT >= 5 and numT < 9:
            outcome += 'L' + 'X' * (numT - 5)
        elif numT == 4:
            outcome += 'XL'
        elif numT > 0 and numT < 4:
            outcome += 'X' * numT
        else:
            pass
        num = num % 10

        numT = num
        if numT == 9:
            outcome += 'IX'
        elif numT >= 5 and numT < 9:
            outcome += 'V' + 'I' * (numT - 5)
        elif numT == 4:
            outcome += 'IV'
        elif numT > 0 and numT < 4:
            outcome += 'I' * numT
        else:
            pass

        return outcome