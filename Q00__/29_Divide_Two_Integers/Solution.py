class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        else:
            sign = ''
            if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
                sign = '-'
            dividend = abs(dividend)
            divisor  = abs(divisor)
            if dividend < divisor:
                return 0
            else:
                listCnt = [ 1 ]
                listNum = [ divisor ]
                while True:
                    if listNum[ -1 ] > dividend:
                        break
                    else:
                        listCnt.append( listCnt[-1] + listCnt[-1] )
                        listNum.append( listNum[-1] + listNum[-1] )

                listCnt.pop()
                listNum.pop()
                sumCnt = listCnt[-1]
                sumNum = listNum[-1]
                for i in range(len(listCnt)-2, -1, -1):
                    if listNum[i] + sumNum == dividend:
                        sumCnt += listCnt[i]
                        break
                    elif listNum[i] + sumNum > dividend:
                        # skip
                        pass
                    else:
                        sumNum += listNum[i]
                        sumCnt += listCnt[i]

                if sign == '-':
                    return 0 - sumCnt
                else:
                    if sumCnt > 2**31 -1:
                        sumCnt = 2**31 -1
                    return sumCnt
