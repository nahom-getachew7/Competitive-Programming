class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = 0
        nums.sort()

        i= 0
        j= 0
        sum=0
        while j < len(nums):
            sum += nums[j]

            while nums[j]*(j-i+1) > sum + k:
                sum -= nums[i]
                i += 1
            freq = max(freq, j-i+1)
            j += 1
        return freq