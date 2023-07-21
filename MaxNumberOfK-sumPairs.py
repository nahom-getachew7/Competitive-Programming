class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i = 0
        j = len(nums) - 1
        
        while i < len(nums) and i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k and j >= 0:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
        return count