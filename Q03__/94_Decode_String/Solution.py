class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numString = ""
        for char in s:
            ordValue = ord(char)
            if ordValue >= 48 and ordValue <= 57:
                # number
                numString += char
            elif char == '[':
                stack.append( int(numString) )
                stack.append("[")
                numString = ""
            elif (ordValue >= 65 and ordValue <= 90) or (ordValue >= 97 and ordValue <= 122):
                # letter (uppercase and lowercase)
                stack.append(char)
            elif char == ']':
                txtString = ""
                while True:
                    tmp = stack.pop()
                    if tmp == '[':
                        break;
                    else:
                        txtString = tmp + txtString
                num = stack.pop()
                newString = txtString * num
                stack.append(newString)
        out = ""
        for substring in stack:
            out += substring
        return(out)