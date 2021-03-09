class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str( int(numerator/denominator) )
        else:
            sign = ''
            if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
                sign = '-'

            numerator = abs(numerator)
            denominator = abs(denominator)

            numLeading = str(numerator // denominator)
            numLeft = numerator % denominator
            listVal  = []
            listLeft = [ numLeft ]
            finiteNum = False
            while True:
                numLeft *= 10
                numA = numLeft % denominator
                numB = numLeft // denominator
                listVal.append( str(numB) )
                if numA == 0:
                    finiteNum = True
                    break
                else:
                    if numA in listLeft:
                        break
                    else:
                        listLeft.append( numA )
                        numLeft = numA

            if finiteNum:
                return sign + numLeading + '.' + ''.join(listVal)
            else:
                repeatLen = len(listLeft)
                repeatBgnIdx = listLeft.index(numA)
                if repeatBgnIdx == 0:
                    return sign + numLeading + '.(' + ''.join(listVal[:repeatLen]) + ')'
                else:
                    return sign + numLeading + '.' + ''.join(listVal[:repeatBgnIdx]) + '(' + ''.join(listVal[repeatBgnIdx:repeatLen]) + ')'
