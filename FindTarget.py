class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        mar = []
        nums.sort()
        for i in range (len(nums)):
            if nums[i] == target:
                mar.append(i)
        return mar