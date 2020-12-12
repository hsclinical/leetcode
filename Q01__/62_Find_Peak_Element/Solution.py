class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(nums[-1]-1)
        nums.insert(0, nums[0]-1)

        for i in range(len(nums)-2):
            if nums[i+1] > nums[i] and nums[i+1] > nums[i+2]:
                return i
