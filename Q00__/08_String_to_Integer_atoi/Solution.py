class Solution:
    def myAtoi(self, s: str) -> int:
        outcome = ''
        sign = '+'
        status = 0

        for i, char in enumerate(s):
            if status == 0:
                if char == ' ':
                    pass
                elif char == '+' or char == '-':
                    sign = char
                    status = 1
                elif char >= '0' and char <= '9':
                    outcome += char
                    status = 2
                else:
                    status = 3
                    break
            elif status == 1:
                if char >= '0' and char <= '9':
                    outcome += char
                    status = 2
                else:
                    status = 3
                    break
            elif status == 2:
                if char >= '0' and char <= '9':
                    outcome += char
                else:
                    status = 3
                    break

        if outcome == '':
            return 0
        else:
            num = int(outcome)
            if sign == '-':
                num = (-1) * num
            if num < -2147483648:
                num = -2147483648
            elif num > 2147483647:
                num = 2147483647
            return num