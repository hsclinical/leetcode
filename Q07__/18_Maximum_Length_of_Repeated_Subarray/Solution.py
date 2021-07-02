class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Len = len(nums1) + 1
        nums2Len = len(nums2) + 1
        matrix = [ [0] * nums1Len for i in range(nums2Len) ]
        maxScore = 0
        for x in range(1, nums1Len):
            for y in range(1, nums2Len):
                if nums1[x-1] == nums2[y-1]:
                    matrix[y][x] = matrix[y-1][x-1] + 1
                else:
                    matrix[y][x] = 0


                if matrix[y][x] > maxScore:
                    maxScore = matrix[y][x]
        return maxScore

