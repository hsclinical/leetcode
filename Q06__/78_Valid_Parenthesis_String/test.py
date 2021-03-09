#!/usr/bin/python

from Solution import Solution
obj = Solution()

#A = "(*))*"
A = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
out = obj.checkValidString(A)
print(out)
