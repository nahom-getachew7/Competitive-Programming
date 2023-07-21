class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    sums.append(i)
                    sums.append(j)
        return sums