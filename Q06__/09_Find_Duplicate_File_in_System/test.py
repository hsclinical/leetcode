#!/usr/bin/python

from Solution import Solution
obj = Solution()

A = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
out = obj.findDuplicate(A)
print(out)
